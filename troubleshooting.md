# Troubleshooting

Outcome: the failure in front of you is
one of the six below, and you know the
check that separates them. All six were
either met by the lab or follow directly
from a mechanism the lab proved; the
transcript is named where one exists.

## "The requested webhook is not registered"

The 404 with the long hint (transcript
t05). Meaning: the workflow exists, its
production address does not — because
the workflow is not **active**.
Fix: switch the workflow on. While
developing, use the **test** URL with
the editor listening instead, and do
not confuse the two addresses:
`/webhook-test/...` is the workbench,
`/webhook/...` is the world.

## The owner setup refuses my password

It names the broken rule in the reply
(transcript t03): at least 8 characters,
a number, and a capital letter. The
lab's readable password failed on the
capital; the same words with one
capitalised passed. If the setup screen
itself is missing, someone (possibly
you, earlier) already created the
owner — sign in, or start from a fresh
user folder if it truly is a new
instance.

## My schedule never fires

Three checks, in order. Is the workflow
**active**? A draft's clock is a drawing
of a clock (chapter 7). Does the
executions list show `trigger` runs for
it at all — or runs that error? Widen
the filter before concluding silence.
And whose clock is it: schedules run in
the **instance's timezone**, which the
lab saw as America/New_York timestamps
inside trigger items on a UTC host. Set
the instance timezone deliberately and
read trigger times in it.

## It ran green and nothing arrived

`success` means the nodes ran — it does
not mean the outside world noticed.
Open the execution and read each node's
output in turn (chapter 5): the usual
findings are a field read from the wrong
level (the payload was under `body`,
chapter 8), a branch the item did not
take, or a last node whose output is
correct and a *destination* that ignored
it. The record tells you which of those
worlds you are in; guessing tells you
nothing.

## The execution I want is missing, or empty

Executions are kept according to the
instance's save and prune settings,
which chapter 12 warned grow teeth:
old runs may be pruned, and some run
kinds are saved with less data than
others. Check the retention settings
before you need the diary, not after.
When reading records through the API on
2.x, remember the stored data field is
a compact linked format — the lab's
`n8n-lab/unflatten.py` is the worked
example of reading it honestly.

## The editor will not load / port already in use

Two different mornings, one shape. If
the address answers nothing: is the
server running? `curl
http://127.0.0.1:5678/healthz` separates
"n8n is down" from "the page is lost",
and the start log's last lines separate
"still starting" from "died". If startup
itself fails with the port taken,
something already owns 5678 — find it,
or move n8n with `N8N_PORT`. And a
sign-in that loops back to the login
screen is usually the session cookie
not surviving — a browser refusing
cookies, or a proxy between you and the
instance rewriting them (chapter 3's
whole model of signing in is that one
cookie).
