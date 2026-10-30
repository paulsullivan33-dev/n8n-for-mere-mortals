# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's data is invented: a visitor, an order for
   notebooks, an example.org address.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: a fair-code licence that is not open source, paid
   tiers above the free core, a single-process SQLite default
   that is a ceiling at scale, execution history that grows
   until pruned, unauthenticated webhooks, workflows as trusted
   code, and vocabulary that changed between 1.x and 2.x.
8. **The ethics rule is in the text, early.** An automation
   acts with its owner's credentials, unattended: chapter 1 and
   the README state that line before any procedure depends on
   it, chapter 9 repeats it at the credential store itself, and
   the webhook chapter states the matching rule for doors —
   an unauthenticated production webhook URL is a capability
   anyone holding it can use, and must be treated like a key.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran. n8n **2.45.6** was
installed unmodified from npm (`npm install n8n`, Node 24.22.1)
into `~/workspace/n8n-labwork`, which is retained, with its
user folder, for re-verification; the server was stopped at
the end of the lab. The install added 2,352 packages, about
2.9 GB, in 18 minutes under load — a quiet machine will be
much faster, and the guide says install times vary. All
transcripts live in `n8n-lab/transcripts/`; the four lab
workflows are `n8n-lab/wf1.json`–`wf4.json`.

The lab drove n8n through its REST API (`/rest/...`) and its
command line, not by clicking the visual editor. The
workflows those calls stored and ran are the same objects the
editor creates and displays, and the editor itself was
verified answering on loopback; the chapters describe editor
steps in editor terms and say plainly, in the README and
chapter 4, that the lab's hands were the API's. The owner
password printed in transcript t03 belonged to the throwaway
lab instance, which held no real data, no real credentials,
and no longer exists.

Run for real, with transcripts as evidence:

- Environment and versions: Node v24.22.1, npm 10.9.4,
  `n8n --version` 2.45.6, installed size 2.9 GB (t00).
- The npm install itself, its 2,352 packages, and the gist of
  its 370 warnings — peer-dependency notices from the
  LangChain family and funding requests, none fatal (t01).
- Server start, the editor's HTTP 200 and page title, and the
  health endpoint answering `{"status":"ok"}` (t02).
- Owner setup: a first password rejected with the uppercase
  rule quoted verbatim, a compliant password accepted, the
  account confirmed as `global:owner`, login returning the
  `n8n-auth` session cookie (t03).
- Workflow 1 (Manual Trigger → Set → Code) created through
  the API and run: execution 1, mode `manual`, status
  `success`, with per-node run data ending in
  `{"greeting": "Hello, Ada!", "visitsSoFar": 3, "nextVisitWillBe": 4}`.
  The 2.x manual-run call's own lesson is kept: without a
  named trigger it answers 400, *"specify either a trigger to
  start from or a destination node"* (t04).
- Workflow 2 (Webhook → Set) created, then its production URL
  called *before* activation — the verbatim 404 "not
  registered" — then activated (2.x activation names the
  saved `versionId`), then called again with a real `curl`
  POST: the response was the last node's item, envelope,
  `body` order, and both stamped fields, and execution 2,
  mode `webhook`, holds the same per-node record (t05).
- Workflow 3 (Schedule Trigger on cron `* * * * *` → Set with
  a `={{ $now.toISO() }}` stamp) activated and left alone:
  executions 3 and 4, both mode `trigger`, at consecutive
  minute marks, the Set node's stamp 130 ms after its minute.
  Both live workflows were then deactivated through the API.
  The same transcript covers the CLI: `export:workflow` and
  `import:workflow` round-tripping workflow 1, matched by id
  (t06).
- Workflow 4 (Manual Trigger → HTTP Request) run against the
  instance's own health endpoint on loopback: execution 5,
  and the HTTP Request node's output item `{"status": "ok"}`
  (t07).
- Reading execution records on 2.x: the stored data field is
  a compact linked ("flatted") format, resolved by the lab's
  `n8n-lab/unflatten.py`; every per-node output quoted in
  this guide came out of that resolver, not out of the raw
  text.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The Docker installation route and every container matter:
  the sandbox cannot run containers.
- The visual editor's clicks as clicks: adding nodes on the
  canvas, the test-webhook "listen" interaction, dragging
  fields into expressions. The workflows, executions and
  outputs those teachings rest on were all run; the pointing
  was not.
- Every external-service node and credential (Gmail, Slack,
  spreadsheets, databases, and the rest) and every OAuth
  sign-in flow: no real accounts were used, anywhere.
- Webhook authentication options, reverse proxies and
  production exposure of an instance.
- Trigger kinds beyond Manual, Webhook and Schedule (form,
  chat, email, per-app event triggers, error and workflow
  triggers) — characterised in chapter 7, not run.
- PostgreSQL, queue mode, multiple workers, and all paid-plan
  and enterprise features, including the AI and LangChain
  node family the install carries — mentioned in the limits
  chapter, not graded.
- The neighbour tools of chapter 11 (Node-RED, Zapier, Make,
  Huginn, Windmill and friends) — characterised, not run.

Fixtures are this guide's own and deliberately generic: a
visitor named Ada with three visits, an order for two
notebooks, a minute log that says the clock struck, and a lab
mailbox at example.org. No real service, account, person or
place appears anywhere in the lab.
