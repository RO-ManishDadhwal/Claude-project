# 7. Data Quality Log

Duplicates, contradictions, missing files, failed parses, and anything uncertain.
This is the honest-accounting document: everything the migration could not do
cleanly is recorded here rather than smoothed over.

**Issues recorded: 0**

---

## 7.1 Duplicates

Items appearing more than once across sources. Nothing is deleted; duplicates are
cross-linked so a future consumer can collapse them deliberately.

| ID | Item | Duplicate of | Kind (exact / near) | Difference | Sources |
|----|------|--------------|---------------------|------------|---------|
| — | — | — | — | — | — |

## 7.2 Contradictions

Sources that state incompatible things. **Both versions are shown. Neither is
chosen.**

| ID | Subject | Version A (+ source) | Version B (+ source) | Nature of conflict |
|----|---------|----------------------|----------------------|--------------------|
| — | — | — | — | — |

## 7.3 Missing files and artifacts

Referenced in the sources but not supplied. This is the re-upload list.

| ID | Referenced item | Referenced in | What is known about it | Needed for |
|----|-----------------|---------------|------------------------|------------|
| — | — | — | — | — |

## 7.4 Failed parses

Files supplied but not readable, with the actual error.

| ID | File | Format | Error | Retry suggestion |
|----|------|--------|-------|------------------|
| — | — | — | — | — |

## 7.5 Truncated or partial content

Content present but visibly incomplete in the source.

| ID | Item | Where it cuts off | Source |
|----|------|-------------------|--------|
| — | — | — | — |

## 7.6 Uncertain information

Anything recorded with less than full confidence, and why. Items here are marked
`confidence: low` or `medium` in `index.json`.

| ID | Item | Why uncertain | Source | What would resolve it |
|----|------|---------------|--------|------------------------|
| — | — | — | — | — |
