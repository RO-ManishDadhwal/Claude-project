# Secrets Register (redacted)

Locations where credentials or other secrets were detected in the source data.

**This file records only that a secret was found and where. It never contains
the secret itself, in whole or in part.** Redaction is applied at the point of
extraction, before anything is written to disk or committed, so no secret value
enters this workspace, `index.json`, or git history.

**Secrets detected: 0**

---

## Findings

_Empty. No source data has been received yet._

| ID | Kind | Where it appeared | Redacted in workspace? | Action for you |
|----|------|-------------------|------------------------|----------------|
| — | — | — | — | — |

---

## What is treated as a secret

Passwords and passphrases; API keys and client secrets; access, refresh, session,
and bearer tokens; private keys and certificates; database and service connection
strings containing credentials; payment card numbers, CVVs, and bank account
details; government identifiers; one-time codes; and any value the source itself
labels as a credential.

## What gets recorded

- The **kind** of secret (e.g. "API key, provider named in source").
- The **location**: file ID, conversation ID, and locator.
- Nothing else. Not a prefix, not a suffix, not a length, not a hash — anything
  that narrows a brute-force search is itself a leak.

## Action for you

Any credential that appeared in a discontinued account's exported data should be
treated as exposed and **rotated at its provider**, independently of this
migration. This register exists so you know exactly which ones to rotate.
