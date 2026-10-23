"""The items: every core dataflow (data type x purpose x action x source x handling context = 6,272).

Each item carries flags, never filters, so analyses can choose what to include:

- ``leaves_home``: handling context is not ``ppd:householdContext`` (same test as the app's ``leavesHome``).
- ``in_corpus`` / ``corpus_count`` / ``corpus_devices``: the item is declared by one of the researched devices.
- ``plausible``: passes a few sense checks (see ``IMPLAUSIBLE``); implausible items stay in the table.
- ``limits``: which modifiers can make the item acceptable. Retention ``ppd:ephemeral`` for every action;
  ``ppd:inHomeOnly`` and ``ppd:onDeviceOnly`` only for use and inference (taxonomy-05 section 6.7.2).
"""

from __future__ import annotations

import itertools
from pathlib import Path

import pandas as pd

from .taxonomy import ACTIONS, BOUNDARY_ACTIONS, DATA_TYPES, FIELDS, HANDLING_CONTEXTS, PURPOSES, SOURCES

LIMIT_EPHEMERAL = "retention=ppd:ephemeral"
LIMIT_IN_HOME = "processing_boundary=ppd:inHomeOnly"
LIMIT_ON_DEVICE = "processing_boundary=ppd:onDeviceOnly"

# Sense checks. Each is (reason, predicate over an item row). They only set the flag.
IMPLAUSIBLE = [
    # Collecting *into* a public audience is not a collection; publishing is a transfer.
    ("collection into a public audience", lambda r: r.action == "ppd:collection" and r.handling_context == "ppd:publicAudience"),
    # A household-provided value is collected inside the household, not by a third party directly.
    ("household data collected by a third party", lambda r: r.action == "ppd:collection" and r.source == "ppd:householdProvided" and r.handling_context == "ppd:thirdPartyContext"),
    # Advertising inside the household context only, with nothing leaving, is not a meaningful flow.
    ("advertising that never leaves the home", lambda r: r.purpose == "ppd:advertisingAndMarketing" and r.handling_context == "ppd:householdContext" and r.action == "ppd:collection"),
]


def limits_for(action: str) -> list[str]:
    """Modifiers that can make an item acceptable, by action (section 6.7)."""
    return [LIMIT_EPHEMERAL] + ([LIMIT_IN_HOME, LIMIT_ON_DEVICE] if action in BOUNDARY_ACTIONS else [])


def build_items(corpus: pd.DataFrame | None = None) -> pd.DataFrame:
    """All 6,272 core items with their flags. ``corpus`` is the researched flows (load_corpus)."""
    rows = list(itertools.product(DATA_TYPES, PURPOSES, ACTIONS, SOURCES, HANDLING_CONTEXTS))
    items = pd.DataFrame(rows, columns=FIELDS)
    items.insert(0, "item_id", range(len(items)))
    items["leaves_home"] = items.handling_context != "ppd:householdContext"
    items["limits"] = items.action.map(lambda a: "|".join(limits_for(a)))

    reasons = []
    for r in items.itertuples(index=False):
        reasons.append("; ".join(reason for reason, test in IMPLAUSIBLE if test(r)))
    items["implausible_reason"] = reasons
    items["plausible"] = items.implausible_reason == ""

    if corpus is not None and len(corpus):
        grouped = corpus.groupby(FIELDS).agg(corpus_count=("flow_id", "size"), corpus_devices=("device_id", lambda s: "|".join(sorted(set(s)))))
        items = items.merge(grouped.reset_index(), on=FIELDS, how="left")
        items["corpus_count"] = items.corpus_count.fillna(0).astype(int)
        items["corpus_devices"] = items.corpus_devices.fillna("")
    else:
        items["corpus_count"] = 0
        items["corpus_devices"] = ""
    items["in_corpus"] = items.corpus_count > 0
    return items


def load_corpus(path: str | Path) -> pd.DataFrame:
    """The researched device flows snapshot (data/corpus/flows.csv, made by scripts/import_corpus.py)."""
    return pd.read_csv(path)
