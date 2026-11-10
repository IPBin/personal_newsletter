# The Long View

A calm, printable daily paper for Pio: half-letter pages, folded into a booklet,
at most 20 pages ($1.00 at UofT Library).

```
HANDOFF.md           context for a new session (start here)
PLAYBOOK.md          the full step-by-step method and style rules
config.yaml          sources, page budget, delivery — edit this to change the paper
EDITORIAL.md         what goes in and how it's written and designed
RUN.md               the morning procedure the scheduled task follows
paper/               layout engine (HTML/CSS -> PDF with WeasyPrint), maps, glyphs,
                     halftone filters, booklet imposition
collectors/          cloud fetcher for GitHub Actions (RSS, opportunity pages,
                     Luma Toronto, Todoist, picture of the day)
state/memory.json    essays already given in full, opportunities seen, past issues
issues/<date>/       issue.json + paper.pdf + print-booklet.pdf
```

Build an issue: `pip install -r requirements.txt && python -m paper.build issues/2026-11-10/issue.json`

## Printing
Print `print-booklet.pdf` double-sided, **flip on short edge**, fold in half.

## Setup still to do
1. Push this folder to the private repo IPBin/personal_newsletter (session must have it attached).
2. Add `TODOIST_TOKEN` as a repository secret (Settings → Secrets and variables → Actions).
   Never paste the token into a chat.
3. Turn on the "Morning fetch" workflow (Actions tab) and run it once by hand.
4. Create the weekday scheduled task that follows RUN.md.
