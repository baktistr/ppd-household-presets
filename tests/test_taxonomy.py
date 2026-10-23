"""The core term set must match the PPD taxonomy draft and the app."""

import re
from pathlib import Path

import pytest

from ppd_presets.taxonomy import FIELD_TERMS, PROCESSING_BOUNDARY, RETENTION

APP_TAXONOMY = Path(__file__).resolve().parents[2] / "ppd-preference-app" / "shared" / "taxonomy.ts"


def test_core_counts_match_taxonomy_05():
    assert {f: len(t) for f, t in FIELD_TERMS.items()} == {
        "data_type": 7, "purpose": 8, "action": 4, "source": 7, "handling_context": 4}
    assert len(RETENTION) == 2 and len(PROCESSING_BOUNDARY) == 3


@pytest.mark.skipif(not APP_TAXONOMY.exists(), reason="ppd-preference-app is not next to this repository")
def test_terms_match_the_app():
    app_terms = set(re.findall(r"'(ppd:[A-Za-z]+)'", APP_TAXONOMY.read_text()))
    ours = {t for terms in FIELD_TERMS.values() for t in terms} | set(RETENTION) | set(PROCESSING_BOUNDARY)
    assert ours <= app_terms, f"not in the app: {sorted(ours - app_terms)}"
