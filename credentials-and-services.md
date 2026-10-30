# Credentials and Real Services

Outcome: you know where n8n keeps the
keys to other services, what connecting
one really grants, and the one node that
can talk to almost anything without a
dedicated key at all. Check: the lab's
fourth workflow, whose output is in this
chapter, was produced by which node —
and why did it need no credential?

## Nodes for services, credentials for keys

n8n ships with hundreds of service
nodes — mail, chat, spreadsheets,
databases, project tools, and a long
tail. Each knows its service's shape:
what a "message" or a "row" is, which
operations exist. What none of them
knows is *your* account. That part is a
**credential**: you create it once in
the editor's credentials store, telling
it the service and the secret (an API
key, a username and password, or an
OAuth sign-in completed in the browser),
and every node that needs it refers to
it by name.

Two storage facts matter. Stored
credentials are **encrypted** in n8n's
database with an instance encryption
key that lives in the user folder
(chapter 2) — so the user folder is the
crown jewels: back it up, guard it, and
know that losing the key makes every
stored credential unreadable at once.
And exported workflows (chapter 5) do
not carry the secrets: moving a workflow
to a fresh instance means reconnecting
its credentials there, by design.

## What connecting one grants

Chapter 1's catch, made concrete: a
credential is not scoped to the workflow
you made it for. While it lives in the
store, any workflow on the instance can
use it, acting as the account it opens —
sending as you, reading as you — at
whatever hour its trigger fires. The lab
therefore connected *nothing*: no real
accounts were used anywhere in this
guide, and every service node and OAuth
flow is taught from the documentation,
labelled documented-only in
`criteria.md`. Connect your own
services one at a time, with the least
powerful key the job needs, and read the
executions list like it matters — it is
the record of what acted in your name.

## The universal spare key: HTTP Request

One node needs no product-specific
knowledge at all. The **HTTP Request**
node makes an HTTP call — any method,
any address, headers and body you
specify, a credential if the endpoint
wants one — and turns the answer into an
ordinary output item. It is the node for
every service n8n has no box for, and
half the services it does.

The lab proved it against the only
endpoint guaranteed present: n8n's own
health check on loopback. *Lab 4 -
Health Check Client* is a Manual Trigger
wired to one HTTP Request node
(`GET http://127.0.0.1:5678/healthz`),
and its execution (transcript t07)
shows the node behaving exactly as
promised:

```text
Manual Trigger -> [{}]
Ask the Health Endpoint -> [{"status": "ok"}]
```

The endpoint's JSON became the item —
the same shape a spreadsheet node or a
mail node would hand on. That is the
answer to this chapter's check, and the
shape of a hundred real jobs: the APIs
guide in this series teaches the HTTP
itself; this node is where that
knowledge plugs into a chain.
