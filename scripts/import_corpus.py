"""Snapshot the researched device flows from ppd-preference-app into data/corpus/flows.csv.

    python scripts/import_corpus.py [path/to/ppd-preference-app]

The app's fixtures (public/mock/devices/*.json) come from the research workbook. The snapshot is committed so
the notebooks run without the app repository; rerun this after the fixtures change.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["data_type", "purpose", "action", "source", "handling_context"]


def main() -> None:
    app = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "ppd-preference-app"
    mock = app / "public" / "mock"
    library = json.loads((mock / "library.json").read_text())["devices"]
    out = ROOT / "data" / "corpus" / "flows.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["device_id", "device_name", "flow_id", "title", "phase", "evidence", *FIELDS, "retention", "processing_boundary"])
        for entry in library:
            device = json.loads((mock / "devices" / f"{entry['id']}.json").read_text())
            for flow in device["flows"]:
                t = flow["taxonomy"]
                c = t.get("constraints") or {}
                w.writerow([device["id"], device["name"], flow["id"], flow["title"], flow.get("phase", ""), flow.get("evidence", ""),
                            *[t[k] for k in FIELDS], c.get("retention", ""), c.get("processing_boundary", "")])
                count += 1
    print(f"wrote {count} flows from {len(library)} devices to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
