"""Write and read the dataset (data/): items, households, answers, decisions, and the data card."""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from .generate import DECISION_CODES, Synthetic, decisions_long


def save(out: str | Path, items: pd.DataFrame, synth: Synthetic, answers: pd.DataFrame, cfg: dict, sample: int = 200) -> dict:
    """Writes every file and returns a summary (also written into DATACARD.md)."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    items.to_csv(out / "items.csv", index=False)
    synth.households.to_csv(out / "households.csv", index=False, float_format="%.4f")
    answers.to_csv(out / "answers.csv", index=False)
    np.save(out / "decisions.npy", synth.decisions)
    (out / "decision_codes.json").write_text(json.dumps({str(k): v for k, v in DECISION_CODES.items()}, indent=2) + "\n")

    sample_dir = out / "sample"
    sample_dir.mkdir(exist_ok=True)
    ids = list(range(min(sample, len(synth.households))))
    synth.households.iloc[ids].to_csv(sample_dir / "households.csv", index=False, float_format="%.4f")
    answers.iloc[ids].to_csv(sample_dir / "answers.csv", index=False)
    corpus_items = items.item_id[items.in_corpus].tolist()
    decisions_long(synth.decisions, items, ids, corpus_items).to_csv(sample_dir / "decisions_corpus_items.csv", index=False)
    np.save(sample_dir / "decisions.npy", synth.decisions[ids])

    summary = summarize(items, synth, cfg)
    (out / "DATACARD.md").write_text(datacard(summary, cfg))
    return summary


def load(out: str | Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, np.ndarray]:
    out = Path(out)
    return (pd.read_csv(out / "items.csv"), pd.read_csv(out / "households.csv"),
            pd.read_csv(out / "answers.csv", dtype=str), np.load(out / "decisions.npy"))


def summarize(items: pd.DataFrame, synth: Synthetic, cfg: dict) -> dict:
    d = synth.decisions
    share = {DECISION_CODES[k]: float((d == k).mean()) for k in DECISION_CODES}
    return {
        "households": int(d.shape[0]),
        "items": int(d.shape[1]),
        "items_in_corpus": int(items.in_corpus.sum()),
        "items_plausible": int(items.plausible.sum()),
        "seed": cfg["seed"],
        "decision_share": share,
        "decisions_sha256": hashlib.sha256(d.tobytes()).hexdigest(),
    }


def datacard(s: dict, cfg: dict) -> str:
    shares = "\n".join(f"| `{k}` | {v:.1%} |" for k, v in s["decision_share"].items())
    return f"""# Data card: synthetic PPD household preferences

Generated {date.today().isoformat()} by `notebooks/02_generate_households.ipynb` with `config/generator.yaml`
(seed {s['seed']}). Same config and seed reproduce the same data (decisions SHA-256 below).

## What it is

{s['households']:,} synthetic households and their decision on each of the {s['items']:,} core PPD dataflows
(data type x purpose x action x source x handling context, draft-dsmullen-ppd-taxonomy-05 section 6), plus their
answers to the candidate onboarding questions.

**This is not survey data.** Every decision follows from latent traits and weights we chose; the direction of each
effect comes from Emami-Naeini et al. 2017, 2020 and 2021 (see `config/generator.yaml`), magnitudes are ours.
Use it to build and test the pipeline, and to see which questions matter under these assumptions, not to claim how
real households behave.

## Files

| File | Contents |
| --- | --- |
| `items.csv` | item_id, the five core fields, `leaves_home`, `limits` (modifiers available), `plausible` and reason, `in_corpus`, `corpus_count`, `corpus_devices` |
| `households.csv` | household_id, latent traits (0..1), `children`, sensitivity per data type |
| `answers.csv` | household_id, one column per candidate question (`ppd_presets/questions.py`) |
| `decisions.npy` | uint8 [households x items]; codes in `decision_codes.json` |
| `sample/` | the first 200 households (traits, answers, `decisions.npy`), and `decisions_corpus_items.csv`: their decisions on the items real devices declare, readable (committed to git) |

Items {s['items_in_corpus']} of {s['items']:,} are declared by the researched devices (`data/corpus/flows.csv`);
{s['items_plausible']:,} pass the plausibility checks in `ppd_presets/items.py`. Nothing is filtered out.

## Decision shares (all households x all items)

| Decision | Share |
| --- | --- |
{shares}

Decisions SHA-256: `{s['decisions_sha256']}`

## Known limits

- Weights encode our reading of the literature; `notebooks/06_sensitivity` (planned) varies them.
- Answers are generated from the same traits as decisions, with `answer_noise` = {cfg.get('answer_noise')}; real people
  are less consistent than that.
- "Ask me" never appears as a decision (PPD effects are allow and deny); it appears only as a questionnaire answer.
"""
