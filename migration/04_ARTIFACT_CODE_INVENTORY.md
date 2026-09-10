# 5. Artifact and Code Inventory

Every artifact, code block, script, document, and uploaded file found in or
referenced by the sources.

**Artifacts and files recorded: 0**
**Full content present: 0 · Partial: 0 · Referenced only, content absent: 0**

---

## Inventory

_Empty. No artifacts or files have been received yet._

| ID | Filename / artifact title | Type | Language | Purpose | Dependencies | Full content present? | Source | Stored at |
|----|---------------------------|------|----------|---------|--------------|-----------------------|--------|-----------|
| — | — | — | — | — | — | — | — | — |

---

## Completeness values

- **`full`** — the complete content is present in this workspace and byte-for-byte
  matches the source.
- **`partial`** — some content is present but the source shows it is truncated
  (an elided middle, a cut-off code block, "rest of file unchanged"). The nature
  of the gap is recorded.
- **`referenced-only`** — the source mentions the file or artifact but does not
  contain it. These are also listed in `06_DATA_QUALITY_LOG.md` under missing
  files, and are the primary re-upload list.
- **`unreadable`** — the file was supplied but could not be parsed. The parse
  failure is logged with the error.

## Dependencies

Recorded as the source states them (imports, package manifests, referenced
services, sibling artifacts). Dependencies are **not** resolved or version-guessed
during migration; an unpinned dependency stays unpinned.

## Storage

Files supplied in full are stored under `migration/inbox/` in their original
form and referenced here by relative path. Original filenames are preserved; if
two files share a name, both are kept and disambiguated by their `FILE-` ID.
