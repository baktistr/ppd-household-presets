# PPD household presets

Data and notebooks for building **household privacy presets** for PPD (Privacy Preference Declaration) from
synthetic households, and the **onboarding decision tree** that assigns a household to one of them.

```
core taxonomy items ──► synthetic households ──► clustering ──► K presets (household rules)
       6,272              (thousands)                                 ▲
                              └── answers to candidate questions ──► decision tree (onboarding)
```

The presets end up as rules in the format of [ppd-preference-app](https://github.com/MBA009/ppd-preference-app),
whose compiler turns them into PPD policies for each device. The full plan is in the capstone docs:
`docs/household-presets-clustering-plan.md`.

## Current results (synthetic data)

A household answers **at most 15 questions**: up to 6 concrete situations place it in one of **4 presets** (stage 1, the
onboarding tree), and the rest go to follow-ups on the situations its preset is least sure about (stage 2, the "help me
refine my settings" wizard). Its answers are then written into the preset's rules, so every household ends with its own
policy (43 rules on average). Cross-validated match with households' own decisions:

| | All 6,272 flows | Real-device flows |
| --- | --- | --- |
| One preset for everyone | 73.9% | 87.9% |
| After stage 1 (5.9 situations on average) | 78.6% | 89.1% |
| **After stage 2 (15 questions in total)** | **80.3%** | **90.0%** |

The 4 presets (`export/presets.json`, 30 rules each), from the strictest to the most open. They are **internal**:
households never see or choose a preset (week 9 with CableLabs: a list invites self-perception bias); the questionnaire
assigns it.

| | Preset (internal working name) | Refuses | Allows | Households |
| --- | --- | --- | --- | --- |
| 1 | Strict · no fixing problems or legal duties | 78% | 22% | 19% |
| 2 | Strict · no product improvement or personalization · OK with features | 59% | 41% | 35% |
| 3 | Careful · no ads · OK with security and device details | 40% | 60% | 31% |
| 4 | Relaxed · OK with legal duties and fixing problems | 18% | 82% | 15% |

**How the numbers were chosen** (recorded in `decisions.json`): only k = 2–4 give well-defined profiles (every profile
stable when households are resampled, Hennig 2007, and every pair different on at least 10% of flows; notebook 03); the
elbow of the clustering is at k = 3–4. Among onboarding trees that reach every preset and give each profile's
households their own preset at least half the time, k = 4 at depth 6 matches best once follow-ups are in (notebook
05). Rules per preset are chosen at the knee of a sweep (notebook 04): 30 for k = 4, against an earlier fixed 15 that
cost accuracy. Each household's own profile's preset is given to 64% of households; the preset given agrees with it on
97% of real-device flows. The profiles are mostly strictness levels; preferences about particular data types for
particular purposes come in through stage 2, which asks about single data type × purpose situations.

**Does it depend on our numbers?** Notebook 06 reruns notebooks 02–05 on seven variants of the grade-D assumptions
(concern weight and household spreads ×0.5 and ×1.5, the studies' effects ×0.75 and ×1.25, no data type × purpose fit).
In every variant the data keeps the studies' directions, well-defined profiles exist for k = 2–4 and no more, the rule
chooses k = 4 (six variants) or k = 3 (household spreads ×1.5; near-ties between k = 3 and 4 can flip between runs), the onboarding reaches all of its presets, and the 15 questions beat one
preset for everyone by 5.6–6.4 points on all flows. The number of presets is therefore a property of how continuous
these households are; re-derive it (notebooks 03–05, same rules) once real answers are available.

## The questionnaire

![The onboarding tree: stage 1 situations on the left, the preset each path ends in on the right](export/onboarding-tree.svg)

Every question is a **concrete situation with examples**, e.g. the first one: *"A device sends how you use your
devices (for example, when you switch the lights on, or what you watch on TV) to the company that made it, to send you
alerts and messages (for example, a doorbell or smoke alarm notification). Would you allow this?"* (No / It depends /
Yes). Each stores an example per device class, so the app can show one from a device the household owns. The picture
shortens situations to *data → where it goes, why*. Children are never asked about (week 9: future work).

`export/onboarding.json` holds everything the app needs: the splash text, the tree, each leaf's preset with its ordered
follow-ups and budget (15 minus the stage 1 questions), every question's full wording, and how answers become rules:
a *yes* or *no* splits the preset rule covering that situation and adds the household's answer as its own rule (rules
never overlap, so exactly one decides each flow); *It depends* keeps the preset. Rerunning the questionnaire **starts
over**: the rules are rebuilt from the new answers, replacing manual edits after a warning.

## The matrix

**Households × 6,272 core dataflows.** A dataflow (an *item*) is one combination of the core `ppd:` terms of
draft-dsmullen-ppd-taxonomy-05 §6:

| Field | Terms |
| --- | --- |
| data type | 7 |
| purpose | 8 |
| action | 4 |
| source | 7 |
| handling context | 4 |

7 × 8 × 4 × 7 × 4 = **6,272 items**.

Each cell holds one decision:

| Decision | Applies to |
| --- | --- |
| `deny` | every item |
| `allow` | every item |
| `allow_if:retention=ppd:ephemeral` (not kept) | every item |
| `allow_if:processing_boundary=ppd:inHomeOnly` | `use` and `inference` only (§6.7.2) |
| `allow_if:processing_boundary=ppd:onDeviceOnly` | `use` and `inference` only |

The qualifiers are **modifiers on the answer**, not extra columns, so the matrix stays 6,272 wide. There is no
"ask me" decision: PPD rules are allow or deny. "Ask" appears only as a questionnaire answer.

Vendor terms (e.g. `sdl:powerState`) never enter the matrix: they are reduced to their core term first, so every
vendor's flows land in one of these 6,272 cells.

## How this follows the PPD drafts

Checked against draft-dsmullen-ppd-protocol-04 and draft-dsmullen-ppd-taxonomy-05 (in the capstone's `docs/ietf-drafts/`).

| Design choice | Draft text |
| --- | --- |
| **One decision per 5-field combination** | A policy rule has one value per core dimension and an effect (protocol §7.11); "an Effective Policy Object SHOULD NOT contain two Policy Rule Objects with the same core dimensions but different effect values" (§7.11). So 6,272 is the policy's own granularity: one rule per item at most. |
| Decisions are allow / deny | Rule effect is "currently one of allow or deny" (§7.11). "Ask" is not a PPD effect, so it is not a decision here. |
| **Qualifiers refine a decision, they are not columns** | Constraints are "structured qualifiers that refine the rule" (§7.11–7.12) and "qualifiers on atomic dataflows" (taxonomy §6.7). `allow_if:retention=ppd:ephemeral` is one rule: `effect: allow`, `constraints: {retention: ppd:ephemeral}`. |
| Retention limit on every action | Retention is defined for collection, use, transfer and inference, with a meaning per action; for transfer it is the receiving side's persistence (taxonomy §6.7.1). `ppd:ephemeral` = "not intended to result in durable persistence". |
| Processing-boundary limits only on use and inference | "processing-placement qualifier for use or inference within the declared handling context" (protocol §7.12; taxonomy §6.7.2); a qualifier "outside its defined applicability" is invalid (taxonomy §6.7). |
| In-home / on-device processing keeps the handling context | The boundary narrows where a use or inference executes *within* the handling context; it does not replace it (taxonomy §6.6, §6.7.2). The generator treats it as lowering exposure, not as moving the flow home. |
| `ppd:indefinite`, `ppd:approvedRemoteProcessing` are not limits | They do not make a flow more acceptable (taxonomy §6.7.1–6.7.2). |
| Plausibility: `ppd:publicAudience` only with `transfer` | Public audience is "a disclosure context" (taxonomy §6.6); only transfer discloses (§6.4). Flag only; nothing is removed. |
| Vendor terms reduce to core before the matrix | Non-core terms must be "reducible to the shared core semantic model" (protocol §7.1); action is flat and needs an exact meaning (taxonomy §6.4). |

**Known gaps against the drafts:**
- A cell holds **one** limit; a rule's constraints may carry several qualifiers at once (e.g. not kept *and* in-home only).
- **Jurisdiction** (taxonomy §6.7.3: a scope plus country/subdivision codes) is not modelled.
- Processing boundary supports broader/narrower terms (§6.7.2); the matching of "in-home only" against a declared
  "on-device only" (narrower, so it should satisfy it) is for the preset/compiler step, not the dataset.

## Notebooks

| Notebook | Status | What it does |
| --- | --- | --- |
| `01_items.ipynb` | done | The core terms, why the grid is 6,272, qualifiers as conditions, the plausibility flag, the real-device corpus, device classes and their fit cells (household model only; PPD has no device field); checks; writes `data/items.csv`, `data/corpus/device_classes.csv`, `data/corpus/device_fit.csv` |
| `02_generate_households.ipynb` | done | **A** evidence → parameters: study effects mapped to PPD terms (`references/crosswalk.csv`), pooled and graded A–D, written to `data/parameters.json`; **B** the generator: a mixed-effects logistic model (study effects, a data type × purpose fit table, one primary data type × purpose concern type per household, household effects per purpose, data type and handling context, device-class fit), β0, spread and noise calibrated to the studies; **C** candidate questions: realistic situations with examples per device class, answered from each household's own decisions (no children question); **D** checks against the studies; writes `data/` and the data card |
| `03_clustering.ipynb` | done | Profiles following Smullen et al. 2020, with k-means (Ward and average linkage compared): k = 1–40, 5-fold cross-validation, 80% agreement threshold, no-ask fallbacks; **well-defined profiles** (bootstrap stability per profile, Hennig 2007, and distinctness, saved as `data/profiles/quality.csv`); comparison with S20's accuracy and overlap and Liu's cluster sizes; saves `data/profiles/` for k = 2–24 |
| `04_presets.ipynb` | done | Profiles → presets: fill low-agreement items with a no-ask fallback, compress 6,272 decisions into non-overlapping rules with the **rule count chosen at the knee of a sweep** (5–160 rules), measure fidelity and household match, compare fallbacks; saves `data/presets/` for k = 2–24 |
| `05_onboarding_tree.ipynb` | done | Stage 1: decision trees from the candidate answers to a preset, for every k and depth (5-fold cross-validation); **stage 2: follow-ups** on the cells the leaf's two most likely profiles are least sure about, within a 15-question cap; k and depth chosen among trees that reach every well-defined profile, by match after follow-ups (`decisions.json`); confusion matrix, robustness, flowchart (`reports/onboarding-tree.svg`); saves `data/onboarding_tree.json` |
| `06_sensitivity.ipynb` | done | Reruns notebooks 02–05 unchanged on seven variants (concern weight and household spreads ×0.5/×1.5, study effects ×0.75/×1.25, no data type × purpose fit) and compares directions, well-defined k, the chosen (k, depth) and the questionnaire's gain over one preset |
| `07_export.ipynb` | done | Writes `export/presets.json` (internal presets, rules with plain-language titles), `export/onboarding.json` (splash, tree, follow-ups, questions with examples, how answers become rules) and `export/onboarding-tree.svg`; checks the exported files reproduce every preset, that writing every household's answers into the rules gives exactly notebook 05's result, and that one rule decides every flow |

## Run it

Needs Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
make setup        # uv sync: creates .venv
make notebooks    # runs the notebooks in order: writes data/ and runs the checks inside them
make lab          # opens Jupyter Lab on notebooks/
```

**All code is in the notebooks**, with an explanation before each step; there is no separate package. Each notebook
ends its steps with `assert` checks, so running the notebooks is the test. Run 01 before 02 (02 reads `data/items.csv`).

`data/` is generated and gitignored, except `data/corpus/` (the researched device flows) and `data/sample/`
(the first 200 households). Same notebooks and seed give the same data; the data card records a hash of the decisions.

## Layout

```
notebooks/01_items.ipynb                  core terms, the items, flags, the corpus (refreshed from ../ppd-preference-app if present)
notebooks/02_generate_households.ipynb    evidence → parameters, the generator, answers, checks
references/                               the studies (PDFs, local), extracted tables, crosswalk.csv (study terms → PPD terms)
data/parameters.json                      every effect with its value, grade and sources, committed
decisions.json                            the chosen k and depth (k = 4, depth 6) with the reason, read by notebooks 03-05; 05 checks it against its rule, committed
data/corpus/device_classes.csv, device_fit.csv   device classes for the household model, committed
data/corpus/flows.csv                     88 flows from 4 researched devices (52 distinct items), committed
data/sample/                              first 200 households, committed
export/presets.json, export/onboarding.json   what the app uses (notebook 07), committed
export/onboarding-tree.svg                  the onboarding tree as a picture (notebook 07), committed
reports/                                  the tree, follow-ups per leaf and a flowchart, for reading (notebook 05 and by hand)
pyproject.toml, uv.lock, Makefile         environment
```

## How a synthetic household decides (v3)

Each household has **facts** (smart devices and the device classes they are, household size, age band; children follow
household size), a concern and a literacy level, and **household effects** on the log-odds of allowing: an overall
level, one per purpose, one per data type, one per handling context leaving the home, and one per data type × purpose.
For each item (data type *t*, purpose *p*, action *a*, source *s*, handling context *c*):

```
η = β0 + β_type[t] + β_purpose[p] + w[a]·β_context[c] + β_action[a] + β_source[s]       ← from the studies (data/parameters.json)
      + fit, if a device class the household owns needs this (t, p, c) cell                 ← Apthorpe 2018 §4.3, §5.7
      + facts + concern + S · household effects
u = η + τ · noise (shared within a cell, and across the handling contexts of one flow)
```

`allow` if u ≥ 0; otherwise *allow if not kept*, *in-home only* or *on-device only* when that condition lifts u to ≥ 0
(small effects: retention and anonymity are the weakest factors in the studies); otherwise `deny`.

**Where the numbers come from.** Study terms are mapped onto PPD core terms in `references/crosswalk.csv` (a study's
"recipient" is `handling_context` read with `action`, taxonomy-05 §6.6; a named company is a role). Each study's
effects, as differences from a shared baseline term, are pooled per PPD term and graded: A (smart-home study, exact
match), B (looser match), C (other domain), D (our assumption). Three numbers are calibrated: β0 so that 47% of flows
leaving the home are accepted and the spread scale S so that the population's majority answer fits 78% of decisions
(Emami-Naeini et al. 2017), and the noise τ so that redrawing a household's decisions changes about 5% of them
(Liu et al. 2016). Notebook 02's checks rerun the studies' contrasts on the synthetic households (same signs, same
order of terms).

**Data type × purpose** (week 9): a small fit table (data used for a purpose it serves is more accepted, sensitive data
for ads less), and one primary **concern type** per household (recordings, whereabouts, identity, habits, telemetry,
or none; sometimes a weaker second one) that lowers acceptance of the data type × purpose combinations it covers.
Sizes are grade D; the direction follows Apthorpe 2018 §5.7 and the Android profiles of Liu et al., which differ by
which permissions people grant.

**Device classes** (camera, lock & entry, thermostat & sensors, voice assistant, TV & media, light & plug, appliance)
are ours: PPD defines none and has no device field, so the household policy stays one decision per item for every
device. A class only makes its fit cells a little more accepted for households that own it.

**This is not survey data.** Most household spreads and several terms no study covers are grade D; the data card lists
them, and the sensitivity notebook must vary them.

## Sources

- Emami-Naeini et al. 2017. *Privacy Expectations and Preferences in an IoT World.* SOUPS 2017.
- Emami-Naeini et al. 2020. *Ask the Experts: What Should Be on an IoT Privacy and Security Label?* IEEE S&P 2020.
- Emami-Naeini et al. 2021. *Which Privacy and Security Attributes Most Impact Consumers' Risk Perception and
  Willingness to Purchase IoT Devices?* IEEE S&P 2021.
- Smullen, Feng, Zhang, Sadeh 2020. *The Best of Both Worlds: Mitigating Trade-offs Between Accuracy and User
  Burden in Capturing Mobile App Privacy Preferences.* PoPETs 2020(1). Privacy profiles from hierarchical
  clustering, profiling with decision trees; the method this repository follows.
- Apthorpe, Shvartzshnaider, Mathur, Reisman, Feamster 2018. *Discovering Smart Home Internet of Things Privacy Norms
  Using Contextual Integrity.* IMWUT 2(2).
- Zhang, Feng, Bauer, Cranor, Das, Sadeh 2021. *"Did you know this camera tracks your mood?": Understanding Privacy
  Expectations and Preferences in the Age of Video Analytics.* PoPETs 2021(2).
- Liu et al. 2016. *Follow My Recommendations: A Personalized Privacy Assistant for Mobile App Permissions.* SOUPS 2016.
- Bin Liu 2019. *Can Machine Learning Help People Configure Their Mobile App Privacy Settings?* PhD thesis, CMU.
- draft-dsmullen-ppd-taxonomy-05 (core terms), draft-dsmullen-ppd-protocol-04.

What each study gives the generator: `references/README.md`.
