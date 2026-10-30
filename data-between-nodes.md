# Data Between Nodes

Outcome: you can predict what a node
will hand on before it runs — the skill
under every other chapter. Check: given
chapter 6's webhook request and the
Stamp the Order settings, write down the
item the Set node emits; then compare
with the answer at the end of this
chapter.

## Items, again, with feeling

Nodes talk only in **items**: a list of
JSON objects. A trigger emits the first
list — a button emits `[{}]`, one empty
object (chapter 4); a schedule emits one
item describing the moment; a webhook
emits one item per request, shaped as an
envelope:

```json
{"headers": {...}, "params": {}, "query": {},
 "body": {"item": "notebook", "qty": 2}, ...}
```

Notice the shape: the caller's actual
payload (`item`, `qty`) is not at the
top level. It rides under **`body`**,
because the envelope also carries the
request's headers, parameters and query.
Most "my workflow got nothing" bugs are
a node reading `qty` from the top level
where only `body.qty` exists. The
execution record (chapter 5) settles
every argument about this: it shows the
item as it truly was, node by node.

## The Set node: fields in, fields added

The **Set** node writes fields onto each
item. Two behaviours, both seen in the
lab:

- By default it **keeps the other
  fields**. *Stamp the Order* added
  `desk` and `received` and the envelope
  — `body` included — passed through
  untouched around them. (The workflow
  file sets `includeOtherFields` for
  exactly this.)
- A Set node can also build an item from
  nothing — *Set a Visitor* started from
  the trigger's empty `[{}]` and emitted
  a complete object of its own making.

Each assignment is a name, a type
(string, number, boolean, and more) and
a value. The value can be fixed text, or
an **expression**.

## Expressions: the small formulas

Write `={{ ... }}` where a value goes
and n8n evaluates the inside instead of
taking it literally. Inside, the useful
names include `$json` (the item being
processed), `$now` (the current moment,
a date object with methods), and `$input`
(the incoming list). The lab used
exactly one, in the minute log:

```text
loggedAt  =  ={{ $now.toISO() }}
```

which stamped each run with its own
time — 130 milliseconds after the minute
it belonged to. The editor helps here:
clicking a field from the input panel
into an expression is the normal way to
write them, and the preview shows the
value the expression would produce for
the current item, which is the check to
run before any run at all.

## The Code node: when formulas run out

A **Code** node is a JavaScript function
wearing a node's clothes: it receives
the items (`$input.all()`, `$input.first()`)
and returns the list the next node sees.
Chapter 4's whole computation was seven
lines — read `visitor` and `visits` off
the first item, return one new item with
three computed fields. In n8n 2.x the
code runs in a separate **task runner**
(the startup log's "JS Task Runner"
registering is that machinery), which
keeps your scrap of code at arm's length
from the server — though chapter 12 is
plain that a workflow remains trusted
code on your machine.

Rule of the house: reach for Set and
expressions first, Code second. A chain
a stranger can read from the boxes beats
a chain hiding in a script — that was
the reason for drawing it in the first
place.

## The check, answered

Chapter 6's envelope, plus two stamped
fields, nothing removed:

```json
{"headers": {...}, "params": {}, "query": {},
 "body": {"item": "notebook", "qty": 2},
 "webhookUrl": "http://localhost:5678/webhook/order-desk",
 "executionMode": "production",
 "desk": "web orders", "received": true}
```

That is the exact item the caller got
back — because in chapter 6 the webhook
was set to answer with its last node,
and this is what its last node had.
