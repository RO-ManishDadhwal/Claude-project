#!/usr/bin/env python3
"""Integrity checks for migration/index.json.

Run after every batch, before committing:

    python3 migration/tools/validate_index.py

Checks performed (stdlib only, no third-party dependencies):

  1. index.json parses and carries every required top-level key.
  2. Every entity ID matches its prefix pattern and is unique.
  3. Every cross-reference resolves to an ID that actually exists.
  4. `counts` matches the real length of each collection.
  5. No secrets entry carries a field that could leak the value.
  6. migration_status is only "complete" when the user has confirmed it.
  7. Every markdown file referenced by a project record exists on disk.

Exit status is 0 when clean, 1 when any check fails.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"

COLLECTIONS = {
    "batches": "BATCH",
    "conversations": "CONV",
    "projects": "PROJ",
    "prompts": "PROMPT",
    "files": "FILE",
    "artifacts": "ART",
    "decisions": "DEC",
    "open_items": "TASK",
    "issues": "ISSUE",
    "secrets": "SEC",
}

REQUIRED_TOP_LEVEL = {
    "schema_version", "created_utc", "last_updated_utc", "migration_status",
    "completion_confirmed_by_user", "counts", *COLLECTIONS,
}

# Fields that must never appear on a secrets entry: each one narrows a search
# for the underlying value.
FORBIDDEN_SECRET_FIELDS = {
    "value", "secret", "token", "key", "password", "hash", "digest",
    "prefix", "suffix", "length", "sample", "excerpt", "snippet",
}

# Keys whose values are ID references to other records.
REF_FIELDS = {
    "project_id", "conversation_id", "duplicate_of", "supersedes",
    "superseded_by", "batch_id",
}
REF_LIST_FIELDS = {
    "decision_ids", "prompt_ids", "artifact_ids", "file_ids", "open_item_ids",
    "issue_ids", "secret_ids", "conversation_ids", "related_ids",
    "conflicts_with", "referenced_in", "files_processed", "files_failed",
}

ID_RE = re.compile(r"^(CONV|PROJ|PROMPT|FILE|ART|DEC|TASK|ISSUE|SEC|BATCH)-[0-9]{2,}$")

problems: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def main() -> int:
    if not INDEX.exists():
        print(f"FAIL: {INDEX} does not exist")
        return 1

    try:
        data = json.loads(INDEX.read_text())
    except json.JSONDecodeError as exc:
        print(f"FAIL: index.json is not valid JSON: {exc}")
        return 1

    missing = REQUIRED_TOP_LEVEL - data.keys()
    if missing:
        fail(f"missing top-level keys: {', '.join(sorted(missing))}")

    # --- IDs: format and uniqueness -------------------------------------
    known: set[str] = set()
    for name, prefix in COLLECTIONS.items():
        entries = data.get(name, [])
        if not isinstance(entries, list):
            fail(f"{name}: expected a list, got {type(entries).__name__}")
            continue
        seen: set[str] = set()
        for i, entry in enumerate(entries):
            if not isinstance(entry, dict):
                fail(f"{name}[{i}]: expected an object")
                continue
            eid = entry.get("id")
            if not eid:
                fail(f"{name}[{i}]: missing id")
                continue
            if not eid.startswith(prefix + "-"):
                fail(f"{name}[{i}]: id {eid!r} does not use the {prefix}- prefix")
            if not ID_RE.match(eid):
                fail(f"{name}[{i}]: id {eid!r} is malformed")
            if eid in seen:
                fail(f"{name}: duplicate id {eid!r} — IDs are never reused")
            seen.add(eid)
            known.add(eid)

    # --- Cross-references resolve ----------------------------------------
    for name in COLLECTIONS:
        for entry in data.get(name, []):
            if not isinstance(entry, dict):
                continue
            eid = entry.get("id", "?")
            for field in REF_FIELDS:
                ref = entry.get(field)
                if ref and ref not in known:
                    fail(f"{eid}.{field} points at unknown id {ref!r}")
            for field in REF_LIST_FIELDS:
                refs = entry.get(field) or []
                if not isinstance(refs, list):
                    fail(f"{eid}.{field}: expected a list")
                    continue
                for ref in refs:
                    if ref not in known:
                        fail(f"{eid}.{field} contains unknown id {ref!r}")
            src = entry.get("source_ref")
            if isinstance(src, dict):
                fid = src.get("file_id")
                if fid and fid not in known:
                    fail(f"{eid}.source_ref.file_id points at unknown id {fid!r}")

    # --- Counts reconcile -------------------------------------------------
    counts = data.get("counts", {})
    if isinstance(counts, dict):
        for name in COLLECTIONS:
            actual = len(data.get(name, []))
            stated = counts.get(name)
            if stated is None:
                fail(f"counts.{name} is missing")
            elif stated != actual:
                fail(f"counts.{name} says {stated}, collection holds {actual}")

    # --- Secrets carry no leakable fields ---------------------------------
    for entry in data.get("secrets", []):
        if not isinstance(entry, dict):
            continue
        leaked = FORBIDDEN_SECRET_FIELDS & entry.keys()
        if leaked:
            fail(
                f"{entry.get('id', '?')}: secrets entry carries "
                f"{', '.join(sorted(leaked))} — record location and kind only"
            )

    # --- Completion is user-confirmed only --------------------------------
    if data.get("migration_status") == "complete" and not data.get(
        "completion_confirmed_by_user"
    ):
        fail(
            'migration_status is "complete" but completion_confirmed_by_user '
            "is false — completion requires explicit user confirmation"
        )

    # --- Project docs exist ------------------------------------------------
    for entry in data.get("projects", []):
        if not isinstance(entry, dict):
            continue
        doc = entry.get("doc")
        if doc and not (ROOT / doc).exists():
            fail(f"{entry.get('id', '?')}.doc references missing file {doc!r}")

    # --- Report ------------------------------------------------------------
    total = sum(len(data.get(n, [])) for n in COLLECTIONS)
    if total == 0:
        notes.append("index is empty — no source data has been processed yet")

    for note in notes:
        print(f"note: {note}")

    if problems:
        print(f"\nFAIL: {len(problems)} problem(s)")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(f"OK: index.json is internally consistent ({total} record(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
