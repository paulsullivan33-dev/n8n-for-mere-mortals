# Recipes

Outcome: three working patterns, each
already proven in the lab, that between
them cover most of what people actually
automate. Each recipe names the
transcript that proves its parts;
extensions the lab did not run are
labelled, not smuggled in.

## Recipe 1: the webhook inbox

**Pattern.** Something outside can ask;
something inside stamps and keeps the
asking. Chapter 6's *Lab 2 - Webhook
Order Desk*, verbatim:

```text
Webhook (POST, path "order-desk",
         respond with last node)
  → Set (add desk, received)
```

Proven end to end in transcript t05,
including the caller receiving the
stamped item as its answer. This is the
shape for order hooks, form relays,
alerts from other systems, and every
"when X happens over there, start a job
here". Natural extensions — appending
the item to a spreadsheet, posting it to
a chat, branching on a field with an IF
node — use service nodes and credentials
(chapter 9) and are documented-only in
this lab; the chain they extend is the
proven part. Remember the door rule:
the path is a key.

## Recipe 2: the clockwork heartbeat

**Pattern.** A clock fires; a small
visible trace says it did. Chapter 7's
*Lab 3 - Minute Log*:

```text
Schedule Trigger (cron * * * * *)
  → Set (entry text, loggedAt = ={{ $now.toISO() }})
```

Proven unattended in transcript t06:
two executions, mode `trigger`, nobody
present. A heartbeat like this is how
you learn an instance is alive, and its
executions list doubles as a diary of
every hour the machine kept. The useful
grown-up version — *every five minutes,
fetch my service's health endpoint and
log the answer* — is the same chain with
the HTTP Request node (proven alone in
transcript t07) between the clock and
the stamp. That assembled chain was not
itself run in the lab, and this guide
says so; every link in it was.

## Recipe 3: read, compute, hand on

**Pattern.** Take fields off an item,
compute something, emit a new item.
Chapter 4's *Lab 1 - Greeting Counter*:

```text
Manual Trigger
  → Set (visitor = Ada, visits = 3)
  → Code (greeting, visitsSoFar,
          nextVisitWillBe)
```

Proven in transcript t04, down to the
output item. Un-glamorous and everywhere:
totals and taxes, names cleaned and
re-cased, a status mapped to a colour,
tomorrow's date from today's. In a real
workflow the first Set is usually a
service node fetching real rows, and the
node after the Code is another service
receiving the result — the middle,
which is the part that is *yours*, stays
this three-box shape. When the
computation is one field, an expression
(chapter 8) does it without the Code
node; when it is a paragraph of logic,
the Code node earns its place.

## The pattern under the patterns

Trigger, one or two honest boxes, a
record you can open. Every recipe here
is that sentence with different nouns —
which is the real content of this guide:
the tool is small, the records are the
point, and the chains you dare to switch
on are the ones whose diaries you know
how to read.
