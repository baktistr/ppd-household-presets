"""The items: every core dataflow (data type x purpose x action x source x handling context = 6,272).

Why this grid (draft-dsmullen-ppd-protocol-04 section 7.11): a policy rule names one value of each of the five core
dimensions plus an effect, and a policy "SHOULD NOT contain two Policy Rule Objects with the same core dimensions
but different effect values". So a household policy holds at most one rule per item, and one decision per item is
exactly what a policy can express.

Qualifiers are not items. Constraints are "structured qualifiers that refine the rule" (protocol-04 7.11-7.12) and
"qualifiers on atomic dataflows" (taxonomy-05 6.7), so a qualifier refines an item's decision ("allow, refined by
retention=ppd:ephemeral") instead of adding columns.

Each item carries flags, never filters, so analyses can choose what to include:

- ``leaves_home``: handling context is not ``ppd:householdContext`` (same test as the app's ``leavesHome``).
- ``in_corpus`` / ``corpus_count`` / ``corpus_devices``: the item is declared by one of the researched devices.
- ``plausible``: consistent with the term definitions (see ``IMPLAUSIBLE``); implausible items stay in the table.
- ``limits``: qualifier values that can turn a deny into an allow for this item:
  ``retention=ppd:ephemeral`` for every action (taxonomy-05 6.7.1 defines retention for all four actions);
  ``processing_boundary=ppd:inHomeOnly`` / ``ppd:onDeviceOnly`` only for use and inference (taxonomy-05 6.7.2,
  protocol-04 7.12; 6.7: a qualifier "outside its defined applicability" is invalid).
  ``ppd:indefinite`` and ``ppd:approvedRemoteProcessing`` never make a flow more acceptable, so they are not limits.
  Jurisdiction (6.7.3, a scope plus country/subdivision codes) is not modelled yet.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import pandas as pd

from .taxonomy import ACTIONS, BOUNDARY_ACTIONS, DATA_TYPES, FIELDS, HANDLING_CONTEXTS, PURPOSES, SOURCES

LIMIT_EPHEMERAL = "retention=ppd:ephemeral"
LIMIT_IN_HOME = "processing_boundary=ppd:inHomeOnly"
LIMIT_ON_DEVICE = "processing_boundary=ppd:onDeviceOnly"

# Consistency with the term definitions. Each is (reason, predicate over an item row). They only set the flag.
# Only combinations the definitions themselves rule out are listed; anything merely unusual stays plausible.
IMPLAUSIBLE = [
    # taxonomy-05 6.6: ppd:publicAudience is "a disclosure context in which data is made available to the public".
    # Disclosing is a transfer (6.4: "making data available to a different recipient or handling context");
    # collection brings data into the participant's or service's own context, use operates "without disclosing it
    # to a different recipient", and inference derives data.
    ("public audience is a disclosure context; only transfer discloses",
     lambda r: r.handling_context == "ppd:publicAudience" and r.action != "ppd:transfer"),
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
