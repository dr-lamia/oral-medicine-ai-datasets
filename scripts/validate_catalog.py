#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "datasets.csv"
REQUIRED = {
    "dataset_name", "primary_scope", "release_date", "last_verified",
    "patients_or_cases", "images_or_visits", "modalities",
    "patient_level_split", "access", "licence", "original_data",
    "dataset_url", "key_limitation", "promising_research_use",
}


def main():
    with CATALOG.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing columns: {sorted(missing)}")
        rows = list(reader)
    if not rows:
        raise SystemExit("Catalogue is empty")
    names = [r["dataset_name"].strip() for r in rows]
    if len(names) != len(set(names)):
        raise SystemExit("Duplicate dataset_name found")
    for i, row in enumerate(rows, start=2):
        for field in REQUIRED:
            if not row[field].strip():
                raise SystemExit(f"Row {i}: empty required field {field}")
        if not row["dataset_url"].startswith("https://"):
            raise SystemExit(f"Row {i}: dataset_url must use HTTPS")
        if row["original_data"] not in {"Yes", "No", "Mixed", "Unclear"}:
            raise SystemExit(f"Row {i}: invalid original_data value")
    print(f"Validated {len(rows)} dataset records")


if __name__ == "__main__":
    main()
