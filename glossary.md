# Glossary

**Active** — a workflow whose triggers
are armed: its webhooks registered, its
schedules ticking. The opposite state is
a draft, which can still be run by hand.

**Connection** — a wire between two
nodes; data flows along it one way,
from trigger toward the end.

**Credential** — a stored, encrypted
key to another service (an API token, a
password, an OAuth grant), referred to
by nodes by name.

**Cron expression** — the five-field
shorthand for a repeating time: minute,
hour, day of month, month, day of week;
`*` means "every".

**Editor** — n8n's web interface, where
workflows are drawn and executions are
read. Served by the same program that
runs the workflows.

**Execution** — one run of a workflow,
stored as a record: status, mode,
times, and what every node received and
produced.

**Expression** — a small formula in a
field, written `={{ ... }}`, evaluated
per item; `$json`, `$now` and `$input`
are its common names.

**Fair-code** — source-available
licensing that is free to use but not
open source in the OSI sense; n8n's
Sustainable Use License is the example
in this guide.

**Item** — one parcel of data travelling
between nodes: a JSON object. Nodes
receive and emit lists of items.

**Mode** — who started an execution:
`manual`, `webhook`, `trigger`, and a
few others. The fastest first clue in
any investigation.

**Node** — one box in a workflow: one
step of work, or, for a trigger node,
the start.

**Production URL** — a webhook's real
address (`/webhook/...`), live whenever
the workflow is active. See also test
URL.

**Run data** — inside an execution
record, the per-node account of what
went in and what came out.

**Task runner** — in n8n 2.x, the
separate worker process that runs Code
node JavaScript, at arm's length from
the server.

**Test URL** — a webhook's workbench
address (`/webhook-test/...`), live only
while the editor is listening for a test
event.

**Trigger** — the node that starts a
workflow: a button, a clock, a webhook,
a form, an event in another service.

**User folder** — the directory
(default `~/.n8n`, or `N8N_USER_FOLDER`)
holding n8n's database, encryption key
and settings. The instance, in one
back-up-able lump.

**Webhook** — an address other programs
can call over HTTP to start a workflow,
carrying their request as the first
item.

**Workflow** — one automation job,
saved as a drawing of nodes and
connections, plus its settings.
