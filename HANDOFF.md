# Handoff — context from the first session (Nov 9, 2026)

Everything a new Claude session needs to continue *The Long View* without
re-asking Pio. Read this, then `PLAYBOOK.md`, then `EDITORIAL.md`, `config.yaml`, `RUN.md`.

## Who this is for
- **Pio (Ignatius Pio Binawan)**, Toronto (America/Toronto time). Second-year
  University of Toronto Scarborough student, CS + Public Policy. Indonesian (Garuda Scholar).
- **TAISI** (Toronto AI Safety Initiative): operations team member, *not* an executive.
  Helped run the Swarm Alignment Hackathon (Nov 6–8, 2026) and the writing desk.
- Alum: TAISI Technical AI Safety Fellowship (BlueDot curricula), CORDA Democracy Fellowship.
- Interests: technical AI governance, AI security, cybersecurity (TryHackMe), policy
  writing, civic tech. Beginner-to-intermediate in AI safety.
- Gmail: professional.binawan@gmail.com. Never print his phone number or address.

## What he wants (his words, condensed)
- A **printable daily newspaper**, half-letter pages, double-sided booklet,
  **max $1/day = 20 pages**. Final page = a beautiful public-domain artwork
  (he loved the Hiroshige "journey" print — keep "The Road" series going).
- **Escape toxic feeds.** Calm, non-clickbait, non-sensational; epistemic hygiene is #1;
  don't keep him in an AI-safety bubble; Indonesia, Canada, US + broad world news.
- **Human writing.** Several Substack essays printed **in full** each day ("I want to
  feel and experience the art of writing"). Summaries only for the rest, **last 24 hours,
  never repeated**, no podcasts, blurbs rare.
- **Plain language.** "Write as if you're talking to a high-schooler." He found early
  drafts hard to read. The "In plain words, and the other side" boxes are a hit.
- **Opportunities** he'd otherwise miss (AI safety fellowships etc.), comprehensive,
  tailored to his profile, with deadlines. He feels bad when he misses deadlines.
- **To-dos** grouped Academics / TAISI / Misc from Quercus, UofT mail, Slack, Todoist.
- **Design**: personality and images, but not maximalist and not minimalist. Black & white.
- **No "About this paper" page** — house rules, sources and citations go in the email.
- **No blank half-pages, no Notes page.**
- **Tell him before sending any test message** (email/Slack). Drafts are fine.

## Sources and how they're connected
| Source | Status | How |
|---|---|---|
| Google Calendar | connected | connector |
| Gmail | connected | connector; labels **News** (Substack + Visual Capitalist), **UofT** (forwarded UofT mail), **Quercus** (forwarded Canvas notices), **Luma** (Luma emails) |
| Slack | connected (TAISI workspace only) | connector; 11 channels; his user id U0BUX860G10. He's in 3 workspaces; the other 2 need their own connection (on his to-do list) |
| Quercus / UofT Outlook | via Gmail forwarding | He set forwarding on Nov 9; Quercus still needed him to click "Confirm Email: Canvas" (Nov 9) |
| Todoist | **not connected** | Options: Todoist's MCP/connector if available, its Google Calendar sync, or `TODOIST_TOKEN` as a GitHub Actions secret (collectors/fetch.py). He has the API key — never ask him to paste it in chat |
| Discord | skipped | needs a read-only bot added by a server admin; he chose to skip for now |
| Luma (Toronto events) | partial | his own events via the Luma Gmail label; city-wide discovery only via the GitHub Action (unofficial API, best effort) |
| News / opportunity pages | via web fetching | many big outlets are blocked from the sandbox; see PLAYBOOK §3 |

## Infrastructure facts learned the hard way
- **Sandbox network is allow-listed.** Reachable: package registries (pypi, npm),
  github.com API + raw.githubusercontent.com. Blocked: most news sites, Wikimedia,
  Substack image CDN, image hosts, Todoist API, open-meteo. Use web-fetch tools for
  news; use the GitHub Action (`.github/workflows/fetch.yml`) for anything that needs the open web.
- **GitHub:** the first session could not reach Pio's repo (sessions only reach
  repos attached to them). Repo: **https://github.com/IPBin/personal_newsletter** (private).
  The new session must have this repo attached. First job: push this project into it.
- **Email delivery:** Gmail tool *can* send attachments, but the file must be passed
  inline (base64) through the model — impractical for 6–12 MB PDFs. Plan: commit PDFs
  to the repo, email a link + the `email.html` body. (Alternatively shrink PDFs a lot.)
- **Images:** public-domain art comes from raw.githubusercontent.com (the Hiroshige
  set in SIMPLYBOYS/tokaido-pixel). News photos need the GitHub Action (Wikimedia
  picture of the day → `paper/imaging.py` halftone). No photos of public figures.
- Rendering: WeasyPrint (HTML/CSS → PDF), pypdf for booklet imposition, pdftoppm for
  previews. Fonts are bundled in `assets/fonts` (from npm fontsource). Maps from
  `assets/geo` (npm world-atlas). WeasyPrint quirks: flex/table blocks don't split
  across pages; `::first-letter` floats misbehave (use the `.dc` span); SVG
  `paint-order` is ignored (no halo text on maps).

## Status at handoff
- **Done:** layout engine, maps, charts, deadline ruler, booklet imposition, page
  fitter (optional essays dropped/re-added, fallback summaries), email generator,
  Gmail draft of the companion email (in his Drafts, not sent), editorial rules,
  tailored opportunities, proof issue for Tue Nov 10 (3 drafts; proof 3 approved
  direction). Cloud fetcher + workflow written but **never run**.
- **Proof 3 feedback he gave:** liked the back-page art and the plain-words boxes;
  asked for more full essays (done: 3 + ChinAI as summary), no About page (done),
  fix the drop-cap gap and empty spaces (done), tailor opportunities (done).
- **Pending:**
  1. Push project to `IPBin/personal_newsletter`; check `requirements.txt` installs.
  2. Turn on the GitHub Action; add `TODOIST_TOKEN` secret (Pio does this in GitHub settings).
  3. Decide delivery: PDFs in repo + email with link (recommended). Ask before the first send.
  4. Create the weekday scheduled task (~6:30–7:00 am Toronto) that follows RUN.md + PLAYBOOK.md.
  5. Connect Todoist; consider the other 2 Slack workspaces later.
  6. Issue No. 1: back page stop 1 again (Nihonbashi), then +1 per issue (`state/memory.json → back_stop`).

## Update from the second session (Nov 9–10, 2026): read this before the tables above
- **Repo is live.** `main` holds the project; PDFs are committed under `issues/<date>/`. The email links to them.
- **Network.** Pio opened the environment's network access. From the shell, `curl -sSL -A "Mozilla/5.0" <url>`
  reaches news sites, program pages, Open-Meteo, Wikimedia and Todoist. The WebFetch tool still fails here, so read
  pages with curl and strip the tags in Python. Visual Capitalist and some JS-only sites (80,000 Hours, PRISM) block this.
- **Todoist works.** `python collectors/todoist.py` prints open tasks. The key is read from the `TODOIST_TOKEN`
  environment variable only. Never write it to a file, a commit, the paper or an email.
- **Issue No. 1 (2026-11-10) is made.** `issues/2026-11-10/make_issue.py` is the worked example of a real issue:
  research in `parts/`, fetched essay texts, then trimming to fit. The three proof drafts moved to `issues/proof-2026-11-10/`.
- **Essays come from the writer's web page, not retyped.** Fetch the Substack post with curl and keep the body
  paragraphs (drop subscribe pleas, related-post headings, comments). Paywalled posts: print the free part and say so.
- **Page budget that worked:** front 1 · Desk + Opportunities 4 · World 6 · Essays + Newsstand 8 · back 1.
  Sixteen news stories of about 100 words is the ceiling. A long lead essay (1,700 words) leaves room for one more.
- **Fitter fixed.** `paper/build.py → fit` now counts pages the same way the final render does, and a dropped essay's
  fallback summary is counted too. Proof folders no longer rewrite `state/memory.json`.
- **Email carries the notes.** Anything said to Pio rather than printed goes in `issue["email_notes"]` and
  `issue["credits"]` (left-out opportunities, thin sources, art credits). The paper stays a paper.
- **Art.** Pio is open to other public-domain art besides the Hiroshige road series. Wikimedia is reachable now.
- **PDFs are small now** (about 1.2 MB each), so they are emailed as attachments. In `create_draft` /
  `send_message`, an attachment's content is a file reference: `sha256:<hex of the file>:<absolute path>`.
  The connector refuses calls over about 3 MB of files. If attaching fails, send the email with the repo links only.
- **School context** is in `SCHOOL.md` and `QUERCUS_CONTEXT.md` (snapshot of Quercus from Nov 10).
- **Still open:**
  The GitHub Action (`collectors/fetch.py`) is still untested and now less needed, since the session can reach the web.
  Discord and the other two Slack workspaces are not connected.

## Memory file
`state/memory.json` lists every essay already printed in full (Decker, Fukuyama,
Bentham's Bulldog, Jack Clark's story) and every summary given, plus opportunities
seen. Do not reprint those in full or repeat those summaries.

## File map
```
PLAYBOOK.md      full method (read first)       EDITORIAL.md   short rules
HANDOFF.md       this file                       RUN.md         daily procedure (short)
config.yaml      sources, profile, budget        requirements.txt
paper/           build.py (fit + render), email.py, maps.py, glyphs.py, imaging.py,
                 impose.py, style.css, templates/issue.html.j2
collectors/      fetch.py + feeds.yaml (GitHub Action; untested)
.github/workflows/fetch.yml
assets/          fonts, geo data, art (tokaido manifest + processed images)
state/memory.json
issues/2026-11-10/  proof issue: make_issue*.py (worked examples), issue.json,
                    paper.pdf, print-booklet.pdf, email.html
```
Build an issue: `pip install -r requirements.txt` (also needs `pdftoppm`/poppler) then
`python -m paper.build issues/<date>/issue.json && python -m paper.email issues/<date>/issue.json`.
