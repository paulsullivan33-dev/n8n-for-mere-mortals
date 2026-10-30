# The Neighbours

n8n sits in a crowded field — visual
automators, cloud cousins, and the
zero-tool baseline. These are
characterisations from the projects' own
documentation, not benchmarks; the lab
ran n8n only.

## Node-RED: the other workbench

Node-RED (which has its own guide in
this series) is the closest relative:
flows of boxes on a canvas, self-hosted,
yours. The difference is ancestry.
Node-RED grew up wiring *things* —
sensors, MQTT messages, relays — and its
unit of travel is the message, shaped by
you, with function nodes in JavaScript
at the centre of its style. n8n grew up
connecting *services* — accounts, APIs,
webhooks — and its unit of travel is the
item, a stricter parcel that makes
service data easier to inspect and its
editor more guided. Node-RED is Apache
2.0 open source without a commercial
string attached and runs happily on a
Raspberry Pi; n8n is fair-code (chapter
12) and heavier. Houses with devices
tend to end up fluent in Node-RED;
desks full of web apps tend to end up in
n8n; a great many workbenches keep both,
each facing the direction it was born
toward.

## Zapier and Make: the cloud cousins

The famous names sell the same drawing
with the server removed: connect an
account, draw the chain, they run it on
their machines and bill by the task.
For a business gluing two cloud apps,
that trade can be right. Its costs are
the mirror of this guide's premise —
your keys and data live on their
computers, the meter runs per step, the
jobs stop when the subscription does,
and an internal tool on your own network
is out of reach. n8n exists, in large
part, as the answer for people who
wanted the drawing without the tenancy.

## The agent and code-first cousins

Huginn, the older Ruby "agent" system,
watches the web and acts on it through
hand-configured agents in files — a
hacker ancestor of the same idea, with
no canvas and a steeper first hour.
Windmill, Activepieces and friends each
re-cut the trade between drawing,
scripting and hosting. And underneath
them all sits the baseline this guide
opened with: cron plus shell scripts,
zero install, zero licence questions,
and a diary written in log files only
you can read. n8n earns its 2.9 GB
precisely where that baseline frays —
branches, retries, several services, and
runs you must be able to audit
afterwards. For a three-line job with
one destination, the script is still the
honest tool, and chapter 12 does not
pretend otherwise.
