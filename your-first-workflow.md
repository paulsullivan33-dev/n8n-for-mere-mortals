# Your First Workflow

Outcome: a three-node workflow that runs
on demand and produces a computed
greeting. Check: an execution whose last
node output is exactly
`{"greeting": "Hello, Ada!", "visitsSoFar": 3, "nextVisitWillBe": 4}`.

The lab created this workflow through
n8n's REST API rather than by clicking —
the stored workflow is the same one the
editor saves, and transcript t04 is the
evidence. The steps below are the
editor's; the workflow file itself is
`n8n-lab/wf1.json`, which you can import
(Executions aside, workflows travel as
JSON — chapter 5 shows the export and
import commands the lab used) and
compare with your drawing.

## The shape

```text
Manual Trigger → Set a Visitor → Build the Greeting
```

Three node types worth meeting first,
because most workflows are built from
their family and friends:

- **Manual Trigger** — the button. It
  emits one empty item when the workflow
  is run by hand, and exists so you can
  test everything downstream without
  wiring up a real event first.
- **Set** — the field-maker. It adds or
  edits fields on the items passing
  through. No code, just names and
  values.
- **Code** — the escape hatch. A scrap
  of JavaScript that receives the items
  and returns new ones, for anything the
  box-shaped nodes cannot say.

## Build it

1. In the editor, create a new workflow.
   The canvas opens with a prompt to add
   a first step: choose **Manual
   Trigger**.
2. Add a **Set** node after it. Add two
   assignments: `visitor`, a string, set
   to `Ada`; and `visits`, a number, set
   to `3`. Name the node *Set a Visitor*.
3. Add a **Code** node after that. Leave
   its mode at "run once for all items"
   and give it this JavaScript:

```js
const item = $input.first().json;
return [{ json: {
  greeting: 'Hello, ' + item.visitor + '!',
  visitsSoFar: item.visits,
  nextVisitWillBe: item.visits + 1
} }];
```

   Name it *Build the Greeting*, and save
   the workflow with a name of your own —
   the lab called it *Lab 1 - Greeting
   Counter*.

## Run it

Press **Execute workflow**. The canvas
animates the chain, and each node shows
its output. The trigger's output is one
empty item — `[{}]` — which surprises
everyone once: the button contributes
*nothing but the start*. The Set node's
output is the item it manufactured:

```json
[{"visitor": "Ada", "visits": 3}]
```

And the Code node's output is the
computed greeting from the check at the
top of this chapter. In the lab's API
run, the same numbers appear in the
execution record (transcript t04):

```text
Manual Trigger -> [{}]
Set a Visitor -> [{"visitor": "Ada", "visits": 3}]
Build the Greeting -> [{"greeting": "Hello, Ada!", "visitsSoFar": 3, "nextVisitWillBe": 4}]
```

## What you just learned, named

A workflow is data flowing downhill.
The trigger decides when; the nodes
decide what happens to the items on the
way. Nothing in this workflow needed
the workflow to be switched on —
running by hand works on a draft, which
is exactly how you develop: build, run
by hand, read the outputs, adjust. The
switch matters when the *world* is
supposed to start the workflow, which
is chapters 6 and 7. First, chapter 5:
how to prove, after the fact and
without watching, that any of this
happened at all.
