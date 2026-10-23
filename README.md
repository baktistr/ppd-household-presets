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
| `01_items.ipynb` | done | Builds the 6,272 items with flags: leaves the home, declared by a researched device, plausible, which limits apply |
| `02_generate_households.ipynb` | done | 5,000 synthetic households from correlated latent traits; their decisions and questionnaire answers; checks against the literature; writes `data/` and the data card |
| `03_clustering.ipynb` | next | k-medoids / Ward / k-means for k = 3–10; stability, preset fit, interpretability |
| `04_presets.ipynb` | planned | Per-cluster decisions compressed into ≤ 15 household rules; coverage of real device flows |
| `05_onboarding_tree.ipynb` | planned | Decision tree from answers to preset; ≤ 7 questions; against a one-preset baseline |
| `06_sensitivity.ipynb` | planned | Vary the generator weights ±50%; do presets and the first questions hold? |
| `07_export.ipynb` | planned | `presets.json` and the questionnaire for the app |

## Run it

Needs Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
make setup        # uv sync: creates .venv
make notebooks    # runs the notebooks in order and writes data/
make test
.venv/bin/jupyter lab notebooks/
```

`data/` is generated and gitignored, except `data/corpus/` (the researched device flows) and `data/sample/`
(the first 200 households). Same config and seed give the same data; the data card records a hash of the decisions.

## Layout

```
config/generator.yaml      every generator number, with the study its direction comes from
ppd_presets/
  taxonomy.py              core terms (taxonomy-05 §6)
  items.py                 the 6,272 items and their flags
  generate.py              latent traits -> decisions
  questions.py             candidate questions and how households answer them
  dataset.py               write/read data/, the data card
scripts/import_corpus.py   snapshot of the researched device flows from ppd-preference-app
notebooks/                 the analysis, in order
tests/                     taxonomy matches the draft and the app; reproducibility; decision rules
data/corpus/flows.csv      88 flows from 4 researched devices (52 distinct items)
```

## How a synthetic household decides

Traits (each 0–1, correlated): privacy concern, trust in the device maker, aversion to third parties, aversion to
inference, retention sensitivity, how much it values features; plus children in the home. For each item:

```
u = intercept + benefit[purpose] × (0.5 + benefit_orientation)
    − risk_weight × sensitivity[data type] × exposure(recipient, action) × (0.6 + concern)
    − source_term[source] + noise
```

`allow` if u ≥ 0; otherwise the first limit that lifts u to ≥ 0 (not kept, then in-home only, then on-device
only); otherwise `deny`. Traits are continuous, not personas, so clustering has to find structure rather than
recover a planted one.

**This is not survey data.** The direction of each effect comes from the studies below; magnitudes are our
choices, documented in `config/generator.yaml` and tested in `06_sensitivity`.

## Sources

- Emami-Naeini et al. 2017. *Privacy Expectations and Preferences in an IoT World.* SOUPS 2017.
- Emami-Naeini et al. 2020. *Ask the Experts: What Should Be on an IoT Privacy and Security Label?* IEEE S&P 2020.
- Emami-Naeini et al. 2021. *Which Privacy and Security Attributes Most Impact Consumers' Risk Perception and
  Willingness to Purchase IoT Devices?* IEEE S&P 2021.
- draft-dsmullen-ppd-taxonomy-05 (core terms), draft-dsmullen-ppd-protocol-04.
