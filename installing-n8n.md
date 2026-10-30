# Installing n8n

Outcome: n8n installed the official npm
way, running on your machine, with an
owner account you can sign in to.
Checks along the way: a version number
from the program itself, a health
endpoint that answers `{"status":"ok"}`,
and a sign-in that succeeds.

## What you need

n8n is a Node.js program. You need
Node.js 18 or newer (the lab used Node
24.22.1) and npm. If Node is new to you,
the Node.js guide in this series covers
installing and sanity-checking it. The
other official route is Docker — one
container, data in a volume — and for
many people that is the comfortable
route; this lab could not run containers
on its build machine, so the Docker
route is described from the project's
documentation, not demonstrated, and
`criteria.md` says so. Everything after
the install is identical either way.

## The install

Into a folder of its own:

```bash
mkdir n8n-labwork && cd n8n-labwork
npm init -y
npm install n8n
```

The lab's run (transcript t01) added
2,352 packages and took 18 minutes on a
small, busy, shared machine; on a quiet
machine it is a few minutes. Budget disk
as well as time: the installed tree was
about 2.9 GB. npm prints warnings —
peer-dependency notices from the AI
libraries n8n carries, and funding
requests from packages. In the lab's run
none of them stopped or damaged the
install; the finish line is `added 2352
packages` and an exit code of 0. Your
count will differ as versions move.

Prove the program is really there
(transcript t00):

```bash
./node_modules/.bin/n8n --version
# 2.45.6
```

(A global install, `npm install -g n8n`,
puts `n8n` itself on your path instead.
The version check matters more than the
arrangement.)

## First start

n8n keeps everything it owns in its user
folder — database, encryption key,
settings. Default: `~/.n8n`. The lab
pointed it at a folder of its own, which
is a good habit for any trial:

```bash
export N8N_USER_FOLDER="$PWD/userfolder"
export N8N_DIAGNOSTICS_ENABLED=false
./node_modules/.bin/n8n start
```

`N8N_DIAGNOSTICS_ENABLED=false` opts out
of anonymous usage diagnostics; set it
or not, but know it exists. A successful
start ends with (transcript t02):

```text
Version: 2.45.6
...
Editor is now accessible via:
http://localhost:5678
```

Two checks that do not need a browser:

```bash
curl -s http://127.0.0.1:5678/healthz
# {"status":"ok"}

curl -s http://127.0.0.1:5678/ | grep -o "<title>[^<]*</title>"
# <title>n8n.io - Workflow Automation</title>
```

Leave the server running; the rest of
this guide talks to it. To stop it,
Ctrl-C in its terminal.

## The owner account

A fresh instance has no users. Open
`http://localhost:5678` and the editor
walks you through creating the **owner**
account — email address, name, password.
The lab did the same thing through the
setup call the editor itself uses
(transcript t03), and immediately met
the password rules: n8n passwords need
at least 8 characters, a number, and a
capital letter, and the refusal says
which rule you broke:

```text
{"code":"custom","message":"Password must contain at least 1 uppercase letter.","path":["password"]}
```

With a compliant password the account
was created (`role: global:owner`), and
sign-in returned a session cookie
(`n8n-auth`) that the editor — and every
later lab call — presents from then on.
Pick a password you would use for
anything that guards keys, because that
is what this account does: whoever owns
it owns every credential and workflow
the instance will ever hold.

## Where things stand

You have: a server on port 5678, an
editor that loads, an owner who can sign
in, and a user folder you can point at
and back up as one lump. The instance
holds no workflows yet. Chapter 4 builds
the first one.
