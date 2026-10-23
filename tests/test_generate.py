"""Items, reproducibility, and the decision rules."""

import numpy as np

from ppd_presets.generate import ALLOW_IF_IN_HOME, ALLOW_IF_ON_DEVICE, generate, load_config
from ppd_presets.items import build_items, load_corpus
from ppd_presets.questions import answer, question_bank

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]


def small_config(n=300):
    cfg = load_config(ROOT / "config/generator.yaml")
    cfg["n_households"] = n
    return cfg


def test_items_cover_the_grid_and_the_corpus():
    items = build_items(load_corpus(ROOT / "data/corpus/flows.csv"))
    assert len(items) == 7 * 8 * 4 * 7 * 4
    assert items.in_corpus.sum() == 52
    assert not (items.in_corpus & ~items.plausible).any()
    # processing boundary only for use and inference (taxonomy-05 section 6.7.2)
    with_boundary = items[items.limits.str.contains("processing_boundary")]
    assert set(with_boundary.action) == {"ppd:use", "ppd:inference"}


def test_same_seed_same_data():
    items = build_items()
    a, b = generate(small_config(), items), generate(small_config(), items)
    assert np.array_equal(a.decisions, b.decisions)


def test_boundary_limits_only_where_allowed():
    items = build_items()
    d = generate(small_config(), items).decisions
    no_boundary = ~items.action.isin(["ppd:use", "ppd:inference"]).to_numpy()
    assert not np.isin(d[:, no_boundary], [ALLOW_IF_IN_HOME, ALLOW_IF_ON_DEVICE]).any()


def test_more_concern_means_fewer_allows():
    items = build_items()
    s = generate(small_config(1000), items)
    allow_share = (s.decisions == 1).mean(axis=1)
    assert np.corrcoef(s.households.concern, allow_share)[0, 1] < -0.5


def test_every_question_is_answered_with_its_options():
    cfg = small_config()
    s = generate(cfg, build_items())
    ans = answer(s.households, cfg, np.random.default_rng(1))
    for q in question_bank():
        assert set(ans[q["id"]]) <= set(q["options"]), q["id"]


def test_public_audience_only_with_transfer_is_plausible():
    # taxonomy-05 6.6: ppd:publicAudience is a disclosure context; only transfer discloses (6.4).
    items = build_items()
    public = items[items.handling_context == "ppd:publicAudience"]
    assert set(public[public.plausible].action) == {"ppd:transfer"}
    assert items.plausible.sum() == 6272 - 3 * (7 * 8 * 7)
