# 1. Master Index

One row per source (conversation, exported file, or account-data record).
Updated cumulatively after every batch.

**Sources indexed: 0**
**Batches processed: 0**
**Last updated: 2026-09-10 (workspace created; no source data received)**

---

## Index

_Empty. No conversations or files have been uploaded yet._

| ID | Source filename / conversation ID | Date | Title | Project / category | Main topics | Important decisions | Reusable prompts | Files / artifacts mentioned | Follow-up actions |
|----|-----------------------------------|------|-------|--------------------|-------------|---------------------|------------------|-----------------------------|-------------------|
| — | — | — | — | — | — | — | — | — | — |

---

## Column definitions

- **ID** — stable `CONV-` or `FILE-` identifier (see `README.md`).
- **Source filename / conversation ID** — exact name as provided in the export.
  Not renamed, not normalized.
- **Date** — as recorded in the source. If the source carries no date, the cell
  reads `not stated in source`; a date is never inferred from context.
- **Title** — the conversation's own title where the export supplies one;
  otherwise `untitled` plus a descriptive label marked as assigned during
  migration.
- **Project / category** — the Claude Project the conversation belonged to, per
  the export. `unassigned` where the export shows no project.
- **Main topics** — short summary phrases, migration-authored.
- **Important decisions** — `DEC-` IDs, detailed in the relevant project file.
- **Reusable prompts** — `PROMPT-` IDs, full text in `03_PROMPT_LIBRARY.md`.
- **Files / artifacts mentioned** — `FILE-` / `ART-` IDs, detailed in
  `04_ARTIFACT_CODE_INVENTORY.md`. Includes items *referenced but not supplied*,
  which are also logged as missing in `06_DATA_QUALITY_LOG.md`.
- **Follow-up actions** — `TASK-` IDs, detailed in `05_OPEN_ITEMS.md`.

Rows are appended in order of processing and never renumbered.
