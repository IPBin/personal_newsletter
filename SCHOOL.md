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

## What cannot be done from a cloud session (learned Nov 10–11, 2026)

- **No computer use.** A cloud session has no tools to see or control Pio's laptop or
  his Chrome windows. Opening Quercus in Chrome does not help a cloud session.
  Computer use only exists in a session started from the Claude desktop app on that
  computer, or a cloud session with the computer linked through the Devices menu.
- **The 6:45 am scheduled run is a cloud session**, so it must not depend on the laptop
  being open. That is why the calendar feed is the right source for due dates.
- Quercus pages need a UofT login (with 2FA), so `curl` cannot read them.

## Still missing: the back catalogue

Announcements and course pages from before Nov 9, each course's syllabus, and grade
weights have **not** been read by anyone yet. Ways to get them, best first:
1. Calendar feed (above) for all due dates. This covers most of what the paper needs.
2. Pio downloads each syllabus PDF and uploads it to a session; summarise it below.
3. A desktop-app session with computer use, reading Quercus in Chrome, for old announcements.

## Courses seen so far (from Todoist task names only; unverified)

| Course | Seen in Todoist | Notes |
|---|---|---|
| ENGA10 | "ENGA10 Midterm" (Oct 27, still open); "Journal Entries Deadline" (Dec 8) | |
| PHLB18 | "PHLB18 Reading Response" (Nov 9, still open) | |
| unknown course | "Scaffolding Assignment 2" (Nov 2, open), 3 (Nov 23), 4 (Dec 8); "Peer Teaching 2" (Nov 30) | Course not named in Todoist |

Other Todoist items without dates: "Submit everything Coop", "Review Syllabuses".

## Rule for adding assignments to Todoist

Once the feed works: for each Quercus item not already in Todoist (match on course +
title), add a task named `<COURSE> <title>` with the due date and time, in Toronto
time. Never delete or complete Pio's tasks. List what was added in the morning email.
