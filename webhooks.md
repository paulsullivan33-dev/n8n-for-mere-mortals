# Webhooks — Workflows the World Can Call

Outcome: a workflow with a real web
address that other programs can call,
proven by a `curl` from outside n8n
whose answer is the workflow's own
output. Check: the same call, made
*before* switching the workflow on,
answers 404 — and by the end of the
chapter you can say why that is good
news rather than a bug.

## The Webhook node

A **Webhook** node is a trigger that
listens. Give it a method (`GET`,
`POST`, ...) and a **path** — the lab
used `order-desk` — and n8n owns the
address:

```text
http://localhost:5678/webhook/order-desk
```

Whatever arrives — headers, query,
body — becomes the trigger's output
item, in an envelope shaped like this
(the lab's real request, transcript
t05):

```json
{"headers": {...}, "params": {}, "query": {},
 "body": {"item": "notebook", "qty": 2},
 "webhookUrl": "http://localhost:5678/webhook/order-desk",
 "executionMode": "production"}
```

The order itself rides under `body`;
everything else is the wrapping the
request arrived in. Chapter 8 unwraps
it properly.

## Two addresses: test and production

Every webhook has two URLs. The **test
URL** (`/webhook-test/order-desk`) works
only while you press "Listen for test
event" in the editor and watch the
result land on the canvas — a
workbench tool. The **production URL**
(`/webhook/order-desk`) works always,
silently, with runs appearing only in
the executions list — but only while
the workflow is **active**. The lab
called the production address too
early, on purpose and then by genuine
accident of ordering, and kept the
answer:

```text
{"code":404,"message":"The requested webhook \"POST order-desk\" is not registered.","hint":"The workflow must be active for a production URL to run successfully. ..."}
```

Read that 404 as n8n being precise:
the workflow exists, the address does
not — yet. It becomes the first entry
in chapter 13's troubleshooting list
because everyone meets it.

## Switching on, and answering back

The lab's workflow, *Lab 2 - Webhook
Order Desk*, is the webhook wired to
one Set node (*Stamp the Order*) that
adds `desk: "web orders"` and
`received: true` to the item. Two
settings make the demonstration: the
workflow must be activated — in the
editor, the toggle; through the API
(transcript t05), an activation call
that in 2.x names the exact saved
**version** to switch on — and the
webhook's **response mode** must be set
to answer with the *last node* rather
than the default "immediately" (which
replies at once with a fixed "Workflow
was started" message and tells the
caller nothing about the result).

Then the real call:

```bash
curl -s -X POST http://127.0.0.1:5678/webhook/order-desk \
  -H "Content-Type: application/json" \
  -d '{"item":"notebook","qty":2}'
```

and the caller received the last node's
item — envelope, order, and both stamps
— while the executions list gained
execution 2, mode `webhook`, status
`success`, whose record shows each
node's hand-off (chapter 5's check).
A complete circle: an outside program
knocked, the chain ran, the answer came
back, and the diary kept the proof.

## The door rule

A production webhook URL is a doorbell
that also hands over whatever the
workflow does. By default it has **no
authentication**: anyone who learns the
address can ring it, as often as they
like. The Webhook node offers basic and
header authentication options, and a
serious instance belongs behind a
reverse proxy or private network besides
— those arrangements are deployment
territory, documented-only here, but
the rule itself is not optional: *treat
every webhook path like a key*, because
functionally it is one.
