# Inbox

Put exported files here (or attach them to the conversation and they will be
copied in). Files are kept in their original form and under their original
names; a `FILE-` ID is assigned to each on arrival.

**Currently empty.**

## What is useful to upload

A Claude data export is typically delivered as a `.zip` or a small set of JSON
files, commonly including a conversations file, a projects file, and an account
file; the exact names and shapes vary by export. Anything else you have is also
welcome — the processing adapts to whatever actually arrives rather than
assuming a fixed layout. Useful sources include:

- The account data export archive, unmodified.
- Individual conversation exports (JSON, Markdown, HTML, or plain text).
- Project instructions and Project knowledge files.
- Files you uploaded to Claude (documents, spreadsheets, PDFs, code).
- Artifacts saved out of conversations.
- Any prompt collection you keep separately.
- Screenshots, if a conversation exists only as an image.

Partial or messy uploads are fine. Anything unreadable is reported with the
actual error and added to the re-upload list rather than being worked around
silently.

## Before you upload

If an export contains credentials, upload it anyway — secrets are detected and
redacted at extraction, and only the kind and location are recorded, in
`../07_SECRETS_REGISTER.md`. Treat any credential that appears in the export as
exposed and rotate it at its provider regardless of this migration.

## Size

Very large archives are better split across batches. If an archive is too large
to process in one pass, that is reported plainly rather than partially
processed, and the split is agreed with you first.
