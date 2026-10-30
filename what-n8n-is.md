# What n8n Is

You have a job that joins two things: a
form that should become a row somewhere,
a page that should be fetched every hour
and compared with yesterday, a message
that should arrive in one chat when
something happens in another system. The
classic way to build that job is a
script — some glue code, a cron entry,
and a log file you will read exactly
once, the day it silently stops working.
Glue code is not hard. Glue code is
*endless*, and it is invisible while it
works.

**n8n is that glue, drawn instead of
written, and kept where you can see
it.** It is a workflow automation
program: a server you run on your own
machine, with a visual editor in the
browser. A job is a **workflow** — a
chain of boxes called **nodes**. The
first box is a **trigger**: a clock, a
webhook (an address other programs can
call), a form, or a plain button. Each
later box does one step — set some
fields, call a service, run a scrap of
code, branch on a value — and passes the
results along as data. When the chain is
switched on, n8n runs it whenever its
trigger fires, with nobody present, and
writes down an **execution** record for
every run: when, what arrived, what each
box passed to the next, and where it
failed if it failed.

That last part — the record — is half
the reason the tool exists. A cron script
that dies leaves a mystery. An n8n
workflow that dies leaves an execution
you can open, showing the exact data
that reached the exact box that choked.
Chapter 5 teaches you to read those
records, because they are also how you
prove a run *succeeded*.

## A first taste

The lab's first workflow is three boxes:

```text
Manual Trigger → Set a Visitor → Build the Greeting
```

The Set box invents a visitor — the name
`Ada`, a visit count of `3`. The Code box
(a scrap of JavaScript, chapter 4 shows
it) computes what a greeter would say.
The execution record shows what left the
last box:

```json
[{"greeting": "Hello, Ada!",
  "visitsSoFar": 3,
  "nextVisitWillBe": 4}]
```

Nobody would automate a greeter. But
every real automation has this shape: a
start, some fields, a computation, and
data coming out the far end that the
next box — in a bigger workflow, a mail
node, a spreadsheet node, another
webhook — would consume.

## The honest catch, up front

n8n does its work *as you*. The
connections it makes to other services
use credentials you give it — your mail
account, your chat workspace, your
server keys — and a workflow fires
whether you are watching or asleep.
That is the point of the tool, and it is
also the responsibility: a switched-on
workflow is a small employee with your
keys, working nights. This guide
therefore builds everything on invented
data and loopback addresses, teaches the
credential machinery honestly in chapter
9, and leaves every real connection for
you to make deliberately. A second
catch, named now and detailed in chapter
12: n8n is *fair-code*, not open source
in the OSI sense — free to run for your
own purposes, with strings on reselling
it that a normal user will never touch.

## What it is not

It is not a general programming
environment: chains of boxes grow
clumsy where a fifty-line script would
stay clear, and chapter 12 says where
that line sits. It is not a hosted
service unless you choose the vendor's
cloud — this guide runs the
self-hosted program. It is not a
monitoring system, though its execution
history will tell you a great deal about
your automations' health. And it is not
magic about other services: a node for a
service still needs an account and a key
for that service, exactly as a script
would (chapter 9).

## Who it is for

The person with a growing cron table of
glue. The maker whose sensors, chats
and dashboards should be talking to each
other. The small-team operator who keeps
copying data between two web apps by
hand. The common thread is jobs that are
small, numerous, and worth watching —
exactly the jobs that are miserable as
loose scripts and pleasant as drawings
with a memory.
