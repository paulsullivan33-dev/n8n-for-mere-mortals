# Proving It Ran

Outcome: given any workflow, you can
answer three questions from its records
alone — *did it run, how did it end, and
what did each node actually pass on?*
Check: find the lab's webhook execution
in the list below and state its mode and
its last node's output, without having
watched it run.

Automations live or die on this chapter.
An automation you cannot audit is a
rumour with a schedule. n8n's answer is
the **executions list** — in the editor's
left rail — and the record inside each
entry.

## Reading the list

Every execution gets an entry: an id, a
workflow, a start time, a status
(`success`, `error`, `running`, and
friends), and a **mode** that tells you
who started it. The lab's whole diary,
after four workflows and a handful of
runs, read like this in miniature:

```text
id 5 | manual  | success | Lab 4 - Health Check Client
id 4 | trigger | success | Lab 3 - Minute Log
id 3 | trigger | success | Lab 3 - Minute Log
id 2 | webhook | success | Lab 2 - Webhook Order Desk
id 1 | manual  | success | Lab 1 - Greeting Counter
```

The modes are the story: two runs a
person asked for, one a stranger's HTTP
request asked for, and two a clock asked
for. When your automation misbehaves,
filter the list by workflow and read the
modes first — they separate "it never
fired" from "it fired and failed" before
you open anything.

## Inside one record

Open an execution and you get the
workflow diagram with, per node, the
items that went in and came out — the
**run data**. That is the whole audit:
not "the Set node was configured with
`visits = 3`", but "on this run, this
node emitted `{"visitor": "Ada", "visits": 3}`".
Configuration is a claim; run data is
evidence. The check at the top of this
chapter: execution 2's last node,
*Stamp the Order*, emitted the order the
webhook received — `{"item": "notebook", "qty": 2}`
under `body` — with its two stamps
attached: `{"desk": "web orders", "received": true}`
(transcript t05).

The API the lab used exposes the same
records (`GET /rest/executions`,
`GET /rest/executions/<id>`). One 2.x
wrinkle, kept here because auditors hit
it: the stored record's data field is
kept in a compact linked format, not
plain nested JSON, so the lab read it
with a small resolver — `n8n-lab/unflatten.py`,
kept in the repository — rather than
pretending the raw text was the record.

## The command line is a second window

Workflows also travel as files:

```bash
n8n export:workflow --id=<id> --output=wf1-export.json
n8n import:workflow --input=wf1-export.json
```

The lab exported the greeting counter
and imported the file straight back
(transcript t06, part 2): *Successfully
exported 1 workflow*, *Successfully
imported 1 workflow*, and the workflow
list unchanged, because an import
matches on the workflow's id. Exports
are your backups, your version-control
artefacts, and your way to move a
workflow between machines without
re-drawing it. An exported workflow
does **not** carry its credentials'
secrets — those stay in the instance
that made them, which chapter 9 returns
to.

## The habit to build

After any change: run it by hand, then
open the execution and read every node's
output, not just the last one's. Most
automation bugs are visible one node
earlier than the node that complains.
And when a workflow is switched on and
the world is meant to drive it, the
executions list becomes the first place
you look each morning — the diary of a
small employee, written in data.
