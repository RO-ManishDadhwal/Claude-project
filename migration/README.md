# Claude Account Migration Workspace

Purpose: capture the contents of a Claude account that is being discontinued
(conversations, Projects, project instructions, uploaded files, artifacts,
prompts, and other account data) into durable, portable documents.

**Status: awaiting first upload. No source data has been received yet.**

Nothing in this workspace is generated from assumption. Every extracted item
carries a source reference back to the file or conversation it came from. Where
a source is missing, unreadable, or ambiguous, that fact is recorded in
`06_DATA_QUALITY_LOG.md` rather than filled in.

## Deliverables

| # | File | Contents |
|---|------|----------|
| 1 | `00_MASTER_INDEX.md` | One row per source: filename/conversation ID, date, title, project, topics, decisions, prompts, files/artifacts, follow-ups |
| 2 | `01_PERSONAL_WORK_CONTEXT.md` | Consolidated personal and work context |
| 3 | `02_projects/<PROJ-id>-<slug>.md` | Project-by-project knowledge base |
| 4 | `03_PROMPT_LIBRARY.md` | Reusable prompts, original wording preserved |
| 5 | `04_ARTIFACT_CODE_INVENTORY.md` | Artifacts and code: filename, purpose, dependencies, completeness |
| 6 | `05_OPEN_ITEMS.md` | Unresolved tasks, commitments, deadlines, follow-ups |
| 7 | `06_DATA_QUALITY_LOG.md` | Duplicates, contradictions, missing files, failed parses, uncertainty |
| 8 | `index.json` | Migration-ready JSON index with stable IDs and cross-references |
| — | `07_SECRETS_REGISTER.md` | Locations where secrets were detected and redacted (never the secret itself) |
| — | `batches/BATCH_LOG.md` | Per-batch processing report |

## Stable ID scheme

IDs are assigned in order of first encounter and never reused or renumbered,
even if a source is later superseded, deduplicated, or found to be corrupt.

| Prefix | Entity | Example |
|--------|--------|---------|
| `CONV-` | Conversation | `CONV-0001` |
| `PROJ-` | Project / category | `PROJ-0001` |
| `PROMPT-` | Reusable prompt | `PROMPT-0001` |
| `FILE-` | Uploaded or exported file | `FILE-0001` |
| `ART-` | Artifact or code unit | `ART-0001` |
| `DEC-` | Decision | `DEC-0001` |
| `TASK-` | Open item / commitment / deadline | `TASK-0001` |
| `ISSUE-` | Data-quality issue | `ISSUE-0001` |
| `SEC-` | Detected secret (redacted) | `SEC-0001` |
| `BATCH-` | Upload batch | `BATCH-01` |

## Source reference format

Every extracted item records where it came from:

```
[FILE-0007 § conversations.json > conv_id=abc123 > message 14]
[CONV-0012 @ 2025-03-04T09:12Z, turn 3]
```

A source reference names the file ID (and, where the format supports it, a path
or locator inside that file) plus the conversation ID and turn where available.
If only part of a locator is known, the known part is recorded and the unknown
part is left blank — it is not guessed.

## Handling rules

- **Verbatim preservation.** Instructions, requirements, code, formulas, and
  decisions are quoted exactly. Formatting of prompts may be normalized only
  where the change is unambiguously cosmetic (whitespace, list markers, fenced
  code); the original is retained alongside any reformatted version.
- **Conflicts.** When two sources disagree, both versions are recorded with
  their source references and the conflict is logged in
  `06_DATA_QUALITY_LOG.md`. Neither version is silently chosen.
- **Duplicates.** Near-identical items get separate IDs and are cross-linked
  via `duplicate_of`; nothing is deleted.
- **Secrets.** Passwords, API keys, tokens, payment details, and comparable
  credentials are redacted at the point of extraction. Only the fact of the
  finding and its location are recorded, in `07_SECRETS_REGISTER.md`. The secret
  value is never written into this workspace, the JSON index, or a commit.
- **Uncertainty.** Anything inferred rather than stated is marked
  `confidence: low` in `index.json` and listed in the data-quality log.
- **Completeness.** The migration is not described as complete until you
  explicitly confirm that all batches have been provided.

## How to upload

Drop exported files into `migration/inbox/` (or attach them to the
conversation). Supported and expected formats are listed in
`inbox/README.md`. Each processing pass appends a report to
`batches/BATCH_LOG.md` and updates every affected deliverable plus `index.json`.
