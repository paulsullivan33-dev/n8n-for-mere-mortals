# Schedules and Other Triggers

Outcome: a workflow that starts itself
on a clock, with executions to prove
nobody was there. Check: two executions,
one minute apart, both mode `trigger`.

## The Schedule Trigger

The **Schedule Trigger** node starts a
workflow when time says so. Its rule can
be a friendly interval — every 15
minutes, every day at 09:00 — or a
**cron expression**, the five-field
shorthand Unix schedulers have used for
decades: minute, hour, day of month,
month, day of week, with `*` meaning
"every". `* * * * *` is every minute;
`0 9 * * 1` is Mondays at nine.

The lab's *Lab 3 - Minute Log* used the
plainest rule there is — the cron
expression `* * * * *` — feeding one Set
node that writes a line
(`entry: "the clock struck"`) and stamps
it with an expression for the current
moment (`={{ $now.toISO() }}`, chapter 8
unfolds the syntax). Activated and left
entirely alone, it produced
(transcript t06):

```text
executions so far: 2
 id: 4 | status: success | mode: trigger | started: 2026-10-30T05:16:00.056Z
 id: 3 | status: success | mode: trigger | started: 2026-10-30T05:15:00.081Z
```

and inside execution 4, the trigger's
own output item — a small calendar of
the moment it fired — and the stamped
line, timed 130 milliseconds after the
minute:

```text
Write the Line -> [{"entry": "the clock struck", "loggedAt": "2026-10-30T01:16:00.130-04:00"}]
```

Two details worth keeping. First, a
schedule, like a webhook, is armed only
by the workflow being **active** — a
draft with a clock in it is a drawing of
a clock. Second, the trigger's item
carried the instance's timezone
(America/New_York, the sandbox's
setting) while the server's own clock
kept UTC: schedules live in the
instance's timezone, and chapter 13
lists the confusion that causes when the
two are not the one you expect.

The lab switched the workflow off again
afterwards — the same activation switch,
thrown the other way. A ticking lab
clock is a fine proof and a poor
neighbour.

## The rest of the trigger family

One chapter can only demonstrate so
many starts; the family, characterised
from the documentation:

- **Manual Trigger** — the button
  (chapter 4). Development's best friend.
- **Webhook** — an address the world
  calls (chapter 6).
- **Form Trigger** — n8n serves a small
  web form; a submission starts the run,
  carrying the form's fields as the item.
- **Chat Trigger** — a message in a
  chat window starts the run; the front
  door of n8n's AI workflows.
- **Email-reading triggers** (IMAP and
  service-specific) — a new message in a
  mailbox starts the run; needs the
  mailbox's credential, chapter 9.
- **App event triggers** — "a new row
  here", "a new issue there", one per
  connected service, each polling or
  listening with that service's
  credential.
- **Workflow Trigger** — another
  workflow calls this one as a
  subroutine, items in and items out.
- **Error Trigger** — starts an
  error-handling workflow when any
  workflow on the instance fails; the
  beginnings of a fire alarm for the
  diary in chapter 5.

Every one of them answers the same
question — *what starts this?* — and
hands the same kind of item to the same
kind of chain. Learn one chain well and
the triggers become interchangeable
front doors.
