# School context — Quercus, courses and deadlines

How the paper learns about Pio's courses, and what is known so far. Keep this file
current: add what you learn about each course (weights, late rules, recurring
deadlines) so a new session or a new model does not have to rediscover it.

## How school information reaches the paper

| Source | What it gives | How |
|---|---|---|
| Gmail label **Quercus** | New announcements and notices, from Nov 9, 2026 onward | Gmail connector. Canvas forwards to professional.binawan@gmail.com. Nothing older than the day forwarding started. |
| Gmail label **UofT** | Forwarded UofT Outlook mail | Gmail connector |
| **Quercus calendar feed** | Every published assignment, quiz and course event, with due date and time | `python collectors/quercus.py`. Needs `QUERCUS_ICAL_URL` in the environment. **Not set up yet.** |
| **Todoist** | Pio's own task list, the place assignments should end up | `python collectors/todoist.py`. Needs `TODOIST_TOKEN`. |

Secrets (`QUERCUS_ICAL_URL`, `TODOIST_TOKEN`) live only in the cloud environment's
settings. Never write them into a file, a commit, the paper, an email or a chat.

## Updates from Pio (Nov 11, 2026)
- **ENGA10 lecture entries**: write just "ENGA10 lecture" and the room. Do not add the reading or text of the week (e.g. "Mrs Dalloway"). Pio did not ask for it. It came from the reading list in QUERCUS_CONTEXT.md. Same rule for other courses: no lecture topics on the front page unless Pio asks.
- **Google Calendar now has everything**: classes, birthdays and the rest. Use it for the
  front-page "Today" list and the week ahead. The class times in QUERCUS_CONTEXT.md are a fallback only.
- **New assignments and MGEA01 Achieve quiz dates** arrive through Quercus emails (Gmail
  label Quercus). That is the agreed source; the calendar-feed reader (`collectors/quercus.py`)
  is optional and unused.
- **ENGA10 midterm**: the "no submission, no grade" note in QUERCUS_CONTEXT.md is a mistake.
  Do not flag it in the paper.

## What cannot be done from a cloud session (learned Nov 10–11, 2026)

- **No computer use.** A cloud session has no tools to see or control Pio's laptop or
  his Chrome windows. Opening Quercus in Chrome does not help a cloud session.
  Computer use only exists in a session started from the Claude desktop app on that
  computer, or a cloud session with the computer linked through the Devices menu.
- **The 6:45 am scheduled run is a cloud session**, so it must not depend on the laptop
  being open. That is why the calendar feed is the right source for due dates.
- Quercus pages need a UofT login (with 2FA), so `curl` cannot read them.

## The baseline: QUERCUS_CONTEXT.md

`QUERCUS_CONTEXT.md` is a full snapshot of Quercus taken on **Nov 10, 2026** by a Claude
desktop session that Pio signed into Quercus himself. It has the five courses (COPB50,
ENGA10, GGRA30, MGEA01, PHLB18), every open deadline, grading weights, late rules, room
and lecture times, and what was already in Todoist. Read it before writing the Academics
to-dos or the "Needs you" box. It goes stale: anything older than a week or two should be
checked against Todoist and new Quercus emails. To refresh it, Pio runs a desktop session
again (the method is written at the top of that file).

How to use it in the paper:
- **Front-page Academics to-dos**: Todoist is the live list (the snapshot's deadlines were
  added there on Nov 10). Use the snapshot for the detail Todoist lacks: weight, late
  penalty, lock dates, room.
- **Recurring items that are not in Todoist**: MGEA01 Achieve quizzes (one per lecture, due
  the next Thursday 7:00 pm; dates only appear in the instructor's "Update" announcements
  in the Quercus Gmail label) and GGRA30 practical quizzes (Wednesdays, open 1:00 pm,
  close 7:00 pm).
- **Class times for the calendar strip** if Google Calendar has no entry: PHLB18 Mon 10–12
  and tutorial 1–2; GGRA30 Wed 11:10–1 and practical 4:10–5; ENGA10 Wed 1–3; MGEA01 Thu 7–10 pm.
- **Academic integrity**: PHLB18 and ENGA10 forbid AI-written submissions. The paper may
  remind, plan and explain. It never drafts graded work.
- **Tone**: several items are overdue or unsubmitted. State them plainly once, with the
  real consequence (penalty, lock date). No nagging, no judgement.

## Rule for adding assignments to Todoist

Once the feed works: for each Quercus item not already in Todoist (match on course +
title), add a task named `<COURSE> <title>` with the due date and time, in Toronto
time. Never delete or complete Pio's tasks. List what was added in the morning email.
