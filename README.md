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
