# Contributing to Awesome Psychology Tasks

Thank you for your interest in contributing! This list aims to be a comprehensive, well-organized reference for experimental psychology tasks, platforms, and repositories.

## How the list is built

`README.md` is **generated** from structured sources — do not edit it directly. The pieces are:

- `sections/*.md` — hand-edited narrative prose (intro, "Choosing a Platform", "Limitations & Gotchas", "Cross-Domain Tasks", etc.).
- `data/platforms.yaml` — the four platform tables (Open Source, Commercial / Freemium, Survey & Clinical, Hosting & Backend).
- `data/collections.yaml` — the Repositories & Collections table plus replication projects and data repositories.
- `data/source-labels.yaml` — maps the short labels (`PT`, `Ms`, `EF`, `Pv`, …) shown in the Implementations column to entries in the SPA's `community-implementations.json`.
- `paradigms.json` and `community-implementations.json` (in the sibling `library.nccr-ttf-ddg.ch/public/data/` directory) — the canonical paradigm list and the known implementations harvested by the [pipeline](../pipeline/). Each paradigm row in "Tasks by Cognitive Domain" comes from these.

To regenerate the README locally:

```bash
pip install -r scripts/requirements.txt
python scripts/build_readme.py            # writes README.md
python scripts/build_readme.py --check    # CI: exits 1 if README.md is stale
```

## How to Contribute

### Adding a Task (Paradigm)

Tasks live in `paradigms.json` in the SPA. To add one, open a PR against `library.nccr-ttf-ddg.ch/public/data/paradigms.json` with:

```json
{
  "slug": "stroop-task",
  "name": "Stroop Task",
  "domains": ["Attention"],
  "description": "Name the ink color of color-words (e.g., \"RED\" in blue ink). Measures selective attention and inhibitory control.",
  "keyReferences": [{ "citation": "Stroop, 1935" }]
}
```

- **slug** — kebab-case unique identifier; used as the join key with implementations.
- **name** — most-cited name in the literature.
- **domains** — array of cognitive domains (one of: `Attention`, `Memory`, `Executive Function`, `Decision Making`, `Perception`, `Language`, `Social Cognition`, `Learning`, `Emotion`, `Creativity`, `Metacognition`, `Motor Control`, `Numerical Cognition`, `Developmental`, `Clinical / Screening`). A paradigm with multiple domains will appear in each table.
- **description** — 1–2 sentences: what the participant does and what it measures.
- **keyReferences[].citation** — the original or most canonical citation (`Author, Year`).

When the SPA is rebuilt, regenerate the README — the new task appears automatically.

### Adding an Implementation

Implementations live in `community-implementations.json` and are normally written by the [ingestion pipeline](../pipeline/) (PsyToolkit, Pavlovia, jsPsych demos, etc.). To curate one by hand, append a record:

```json
{
  "id": 10999,
  "name": "Stroop Task · Inquisit (Millisecond)",
  "domains": ["Attention"],
  "paradigm": "stroop-task",
  "tier": "community",
  "platform": "inquisit",
  "url": "https://www.millisecond.com/download/library/stroop/",
  "provenance": { "source": "manual", "fetchedAt": "2026-05-07", "verificationResult": "passed", "lastVerifiedAt": "2026-05-07" }
}
```

The README only renders implementations whose `platform` is listed in `data/source-labels.yaml`. To surface a new platform under its own short label (e.g., `[Lv]` for Labvanced), add it there.

### Adding a Platform or Collection

Edit `data/platforms.yaml` (for the four platform tables) or `data/collections.yaml` (for repositories, replication projects, data repositories). Re-run the generator.

Platform fields: `name`, `url`, `description`, `tech`, `online`, `status` (`active` | `maintained` | `legacy`), `timing`, `pricing`. Survey/clinical and hosting tables have a reduced field set — see existing rows.

### Editing Narrative Sections

The "Choosing a Platform" decision tree, "Platform Limitations & Gotchas" notes, and "Cross-Domain Tasks" list are hand-curated — edit the corresponding file under `sections/` and re-run the generator. Do **not** edit `README.md` directly.

## Guidelines

1. **Verify before submitting.** Make sure the task, platform, or repository is not already listed (check the YAML/JSON source, not the README).
2. **Use established paradigms.** Tasks should be well-known in the literature with at least one peer-reviewed publication describing them.
3. **Keep descriptions concise.** One to two sentences per task. Focus on what the participant does and what it measures.
4. **Provide accurate references.** Use the original or most canonical citation.
5. **Check links.** Run `python scripts/check_links.py` before submitting.
6. **Regenerate the README.** Always commit `README.md` alongside changes to its sources so reviewers can see the rendered effect.

## Submitting Changes

1. Fork the repository.
2. Create a new branch (`git checkout -b add-new-tasks`).
3. Edit `sections/`, `data/`, or the upstream `paradigms.json` / `community-implementations.json` as appropriate.
4. Run `python scripts/build_readme.py` to regenerate `README.md`.
5. Commit both the source change and the regenerated README.
6. Submit a pull request with a clear description of what you added or changed.

## Reporting Issues

If you find an error (wrong reference, broken link, incorrect description), please [open an issue](../../issues) describing the problem.

## Code of Conduct

Be respectful and constructive. This is a collaborative academic resource.
