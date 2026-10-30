# The Moving Parts

Outcome: you can name every part of an
n8n instance and say which part holds
what — so when something surprises you
later, you know where to look. Check:
after reading, explain to yourself why
the lab's webhook answered 404 before
its workflow was switched on. (Chapter 6
has the full story; the answer lives in
the last part described below.)

## The workflow

A **workflow** is one job, saved as a
drawing: boxes, the wires between them,
and each box's settings. It lives in
n8n's database, can be exported to a
JSON file (the lab's four live in
`n8n-lab/` in exactly that form), and
can be edited in the browser editor,
created through the API the lab used, or
imported from the command line. A
workflow is a *draft* until it is
switched on — see "active", below.

## Nodes and triggers

A **node** is one step. Most nodes do
work: set fields, call a service, run
code, filter, branch, wait. The special
first kind is the **trigger node**: it
does no work; it decides *when the whole
chain starts*. A Manual Trigger starts
when you press the button. A Schedule
Trigger starts when the clock says so. A
Webhook node starts when a request
arrives at its address. A workflow has
one trigger and as many working nodes as
the job needs; chapter 8 covers the
trigger family.

Wires between nodes are **connections**.
Data flows along them in one direction,
trigger first. A node with two outgoing
wires sends its output down both.

## Items: the parcels

What travels along the wires is a list
of **items**. An item is a small JSON
object — field names and values:

```json
{"visitor": "Ada", "visits": 3}
```

One item is the common case; a node that
fetches a list (a folder of files, a page
of results) emits many items, and most
nodes then run *once per item*. Nearly
everything in n8n becomes easier once
you watch the items: they are the only
thing nodes ever say to each other.
Chapter 8 is devoted to them.

## Executions: the memory

Every run of a workflow — started by
button, clock, webhook or another
workflow — is stored as an
**execution**: its workflow, its start
time, its status, its **mode** (n8n
labels runs `manual`, `webhook`,
`trigger`, and a few more), and the full
record of what each node received and
produced. The executions list in the
editor is the instance's diary. The
lab's proudest moments are entries in
that diary: execution 2, mode `webhook`,
status `success`; executions 3 and 4,
mode `trigger`, fired by a clock with no
human anywhere near.

## Credentials: the keys

A **credential** is a stored key to
someone else's service — an API token, an
OAuth grant, a password. Nodes refer to
credentials by name ("my mail account")
instead of holding the secret in the
workflow drawing, and n8n encrypts
stored credentials with an instance
encryption key kept in its user folder.
Lose that key and the stored credentials
are unreadable — chapter 9 covers the
care and feeding. The lab used no real
credentials at all, so its store stayed
empty and uninteresting, which for a lab
is the right way round.

## The engine, the editor, the database

Three pieces of machinery hold the parts
above. The **server** (the engine) runs
workflows, listens for webhooks, watches
the clock, and serves the **editor** —
the web page where workflows are drawn
and executions read. Both live in one
program started by `n8n start`. Its
memory is a **database**: SQLite by
default, one file in the **user folder**
(`~/.n8n` unless you point
`N8N_USER_FOLDER` elsewhere, as the lab
did). Workflows, executions,
credentials, and your owner account all
live there. Big installations swap in
PostgreSQL and extra worker machines;
that is the vendor's scaling story,
documented-only in this guide, and
chapter 12 names it under limits.

## Active: the switch that matters

A workflow exists in two states. In its
draft state it can be edited and run by
hand for testing, but its triggers are
not armed: its webhook address does not
exist, its schedule does not tick. When
you switch it **active** (in n8n 2.x the
vocabulary leans on *publishing* a
version — the editor's toggle does this
for you), n8n registers the webhook and
starts the clock. The lab proved the
difference with one `curl` each way:
before activation, `POST /webhook/order-desk`
was answered `404 ... not registered`;
after, the same call ran the workflow
and returned its output. Remember this
switch whenever a workflow "does nothing"
— it is the first suspect in chapter 13.
