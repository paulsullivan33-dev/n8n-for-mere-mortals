# n8n for Mere Mortals

Every connected life grows the same weed:
small jobs that join two services
together. When a form is submitted, file
the answer. Every morning, fetch this
and post that. When this webhook knocks,
look something up and reply. Each job is
small enough to write as a script, and
there is always one more of them, and
the scripts pile up in a cron table
nobody fully remembers writing. **n8n**
is the workbench for that weed patch. It
is a workflow automation program you run
on your own machine: you draw each job
as a chain of boxes — a **workflow** —
and n8n runs it when a schedule says so,
when a webhook knocks, or when you press
the button, and keeps a record of every
run that you can open and inspect.

This guide explains how n8n's pieces
fit, how to install it with npm and give
it an owner account, and how to build
three small workflows that between them
cover the tool's whole story: one you
start by hand, one the world starts by
calling a web address, and one a clock
starts on its own. Then it does
something tool tours often skip: it
**proves** the runs happened, by opening
the execution records and reading what
each box actually passed to the next.

The lab that wrote this guide ran the
real thing: **n8n 2.45.6**, installed
from npm on a small Linux machine, its
editor answering on the loopback
address, an owner account created
through its own setup call. Against it
the lab built four workflows — a
by-hand greeting counter (Manual Trigger
→ Set → Code), a webhook order desk that
a real `curl` knocked on, a minute log
that a schedule trigger fired twice,
unattended, while nobody watched, and a
health-check client proving the HTTP
Request node against a live endpoint.
It exported a workflow from the command
line and imported it back. It also broke
things on purpose and kept the receipts:
an owner password the rules refused, and
a webhook called before its workflow was
switched on, answered with a 404 that
explains itself.

What the lab could not do, it did not
fake. It drove n8n through its REST API
and command line rather than clicking
the visual editor, so the editor's
clicks are taught from the workflows
those calls stored — the same workflows
the editor would have saved. It used no
real accounts, so the service nodes that
need one (Gmail, Slack and their many
cousins) and every OAuth sign-in are
taught from the documentation and
labelled as such wherever they appear.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What n8n is**](what-n8n-is.md) —
  the mental model: jobs drawn as chains
  of boxes, run by schedules, webhooks
  and buttons, on your own machine
- [**The moving parts**](the-moving-parts.md) —
  workflows, nodes, items, executions,
  credentials and the database that
  remembers them all — and which part
  holds what
- [**Installing n8n**](installing-n8n.md) —
  the npm install, the user folder, the
  first start, and the owner account
  whose password has rules with teeth
- [**Your first workflow**](your-first-workflow.md) —
  three boxes — Manual Trigger, Set,
  Code — and a greeting that comes out
  the far end
- [**Proving it ran**](proving-it-ran.md) —
  the executions list, the record inside
  each run, and how to read what every
  node passed on
- [**Webhooks**](webhooks.md) — workflows
  the world can call: test and production
  addresses, switching a workflow on, and
  the 404 that means "not yet"
- [**Schedules and other triggers**](schedules-and-triggers.md) —
  the clock as a starting box, cron
  expressions in plain words, and the
  trigger family beyond it
- [**Data between nodes**](data-between-nodes.md) —
  items, the JSON parcels that travel
  the chain, and expressions, the small
  formulas that read and stamp them
- [**Credentials and real services**](credentials-and-services.md) —
  how n8n holds your keys, why the HTTP
  Request node is the universal spare
  key, and what connecting a real
  account means
- [**Recipes**](recipes.md) — a webhook
  inbox that stamps what arrives, a
  clockwork heartbeat, and the
  read-compute-hand-on shape underneath
  most automations
- [**The neighbours**](the-neighbours.md) —
  Node-RED the device wirer, Zapier and
  Make the cloud cousins, and plain cron:
  what each does that n8n doesn't, and
  vice versa
- [**Limits**](limits.md) — the fair-code
  licence, one machine and a small
  database, webhooks that are doors,
  history that grows, and a tool whose
  vocabulary changed between versions
- [**Troubleshooting**](troubleshooting.md) —
  the unregistered webhook, the refused
  password, the schedule that never
  fires, and the successful run where
  nothing arrived
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Connecting your real accounts end to
end. The moment a workflow touches
Gmail, a bank, a workplace chat, it is
acting as you, with your keys, possibly
at 3 a.m. — so this guide teaches the
mechanics on invented data and leaves
each real connection for you to make
deliberately, service by service.
Running n8n as a public, multi-user
platform is likewise out: this is one
person's workbench on one machine.
n8n's AI and LangChain nodes — a large
family riding inside the same install —
get an honest mention in the limits
chapter and no more; they deserve their
own guide, and this lab did not grade
them.

## How to use this guide

Read chapter 1 for the model, and
chapter 2 before installing anything —
knowing which part holds what turns
later surprises into named problems.
Chapters 3 and 4 get you a running
instance and one workflow that answers
to a button. Chapter 5 is the one to
read slowly even if everything seems to
work: its checks are how you catch the
automation that ran green and did
nothing. The lab's transcripts live in
`n8n-lab/transcripts/`; the four lab
workflows are `n8n-lab/wf1.json` to
`wf4.json`, ready to import into your
own instance; and `n8n-lab/unflatten.py`
is the small script the lab used to read
n8n 2.x's stored execution data.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Node-RED for Mere Mortals](https://paulsullivan33-dev.github.io/nodered-for-mere-mortals/)
- [APIs for Mere Mortals](https://paulsullivan33-dev.github.io/api-for-mere-mortals/)
- [Node.js for Mere Mortals](https://paulsullivan33-dev.github.io/nodejs-for-mere-mortals/)
- [MQTT for Mere Mortals](https://paulsullivan33-dev.github.io/mqtt-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/n8n-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/n8n-for-mere-mortals/blob/main/LICENSE-CODE).
