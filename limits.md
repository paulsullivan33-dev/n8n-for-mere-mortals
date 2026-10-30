# Limits

Outcome: you can name what n8n will not
do, will not do for free, and will not
do small — before one of those facts
names itself in production.

## The licence is fair-code, not open source

n8n is distributed under its Sustainable
Use License: source-available, free to
run for your own and your organisation's
internal purposes, and *not* licensed
for taking the product itself and
selling it as a service to others. It is
not an OSI-approved open-source licence.
For the reader of this guide — one
person, one machine, their own jobs —
the practical difference from open
source is zero; for anyone dreaming of
building a business *on* n8n rather than
*with* it, the licence text, not this
guide, is the document to read. Some
features are additionally reserved for
paid plans (the vendor's cloud, and
enterprise self-hosted tiers): advanced
user roles and SSO are the examples the
documentation puts in that bucket. The
core of this guide — workflows, triggers,
executions, the nodes used here — is in
the free self-hosted program the lab
ran.

## One machine, one small database

The default instance is a single
process keeping a single SQLite file.
That is a virtue at this guide's scale
and a ceiling above it: heavy volume,
many workers, and queue-based scaling
mean PostgreSQL and a different run
mode, which this lab did not exercise
and teaches documented-only. The install
itself is not small — about 2.9 GB of
Node packages in the lab — and the
program wants a real machine's worth of
memory when workflows grow teeth. A
Raspberry-Pi-class board is Node-RED
territory (chapter 11), not this tool's
natural home.

## History grows

Every execution is stored — that is the
point — and stored history is data that
accumulates. A workflow firing every
minute fills its diary with 1,440
entries a day. n8n has settings to prune
old executions and cap what is kept;
an instance you switch on and forget
will eventually present the bill as a
swollen database. Set the retention
before the fleet of clocks, not after.

## Webhooks are doors

Production webhooks answer anyone who
knows the address; chapter 6's door
rule. The node's optional authentication
and a proxy in front are arrangements
you add. Treat an unauthenticated
webhook that *does* something — sends,
writes, buys — as an unlatched door
with your name on it.

## Workflows are trusted code

A Code node runs JavaScript with real
power on your machine (2.x fences it
into a task runner, which reduces, not
removes, the trust), and every node acts
with the credentials you connected. The
corollary: an imported workflow file is
a program from the internet. Read one
before you switch it on with the same
care you would give a shell script —
chapter 5's export files included.

## The vocabulary moves

Versions change the furniture. This
guide's lab ran 2.45.6 and met it
directly: activation in 2.x is a
versioned act (the editor's toggle
hides this; the API does not), the
manual-run call changed shape from
earlier versions, and `/rest/me` — a
long-standing endpoint — is simply gone.
Older tutorials will disagree with a 2.x
instance in details like these. Trust
your instance's responses over any
guide's memory, including this one's.

## What it is not for

Long, branchy business logic that a
programmer would rather hold as code;
jobs another tool already does whole
(a backup program backs up better);
and anything whose failure must page a
human *reliably* — n8n's error workflows
help, but the instance is itself a thing
that can be down. The honest summary:
a superb workbench for small jobs
between services, owned by one person
who reads the diary.
