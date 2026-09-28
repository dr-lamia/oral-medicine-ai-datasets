#!/usr/bin/env python3
import csv
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("dataset_url", "publication_url", "code_url")


def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": "oral-medicine-ai-datasets-link-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            return response.status, response.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, url
    except Exception as exc:
        return "ERROR", str(exc)


def main():
    with (ROOT / "datasets.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    failures = []
    for row in rows:
        for field in FIELDS:
            url = row.get(field, "").strip()
            if not url:
                continue
            status, detail = check(url)
            print(f"{row['dataset_name']}\t{field}\t{status}\t{url}\t{detail}")
            if status == "ERROR" or (isinstance(status, int) and status >= 400 and status not in {403, 429}):
                failures.append((row["dataset_name"], field, status, url))
            time.sleep(0.2)
    if failures:
        print(f"\n{len(failures)} link failures", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
