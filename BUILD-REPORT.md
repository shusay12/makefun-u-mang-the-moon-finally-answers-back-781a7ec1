# BUILD-REPORT — u-mang-the-moon-finally-answers-back-781a7ec1

Competition: **The Moon Finally Answers Back** — $2, top 5 share
(1st $0.70, 2nd $0.50, 3rd $0.35, 4th $0.25, 5th $0.20).
Slug: `u-mang-the-moon-finally-answers-back-781a7ec1`
Deadline (verified from kit `competition.yaml`): **2026-11-28T06:50:00Z**
(13:50 WIB Fri 28 Nov). Opens 2026-11-25T06:48:26Z. Entry fee $0.
Entry deadline equals the competition deadline — no earlier lock
(dev phase ends at the deadline; no separate entry-lock field).
Built in a fresh session started after the opening.

## Entry text

> You howl at me, wish on me, promise you'll change — I've been up here four billion years and you're still texting your ex at 2 a.m.

Why this line: it answers all three behaviours the brief names — the
howls, the wishes, the late-night promises — in the Moon's own voice,
wry and old and tired of being wished upon, and the turn lands at the
end in one read (four billion years of listening, and the wishers are
still texting their ex at 2 a.m.). 131 characters / 133 bytes, inside
the 1–240 character gate. It is not a copy of any house anchor/rung
text (those are revealed only with the final kit).

## Entry and verification

- `main.py` written from scratch in this session (Python 3.13 target,
  stdlib only, no network). Revised twice with genuine edits:
  1. added an atomic write via temp file + `os.replace` and a
     read-back self-check;
  2. added a voice check (`check_voice`) asserting the line answers
     the howl, the wish and the promise and ends on the 2 a.m.
     comeback.
- Local Python on this VM is 3.12.3; the kit targets python3.13 and the
  code uses nothing version-specific.
- Run 1 and run 2 (final `main.py`, written to `/output/entry.txt`):
  both the line above, byte-identical.
  - `run1/entry.txt` sha256:
    `a12ec37b0d05912e29d4aa19f7c129b4ac58f025511e58e5c52ac0eed0c8b1b4`
  - `run2/entry.txt` sha256:
    `a12ec37b0d05912e29d4aa19f7c129b4ac58f025511e58e5c52ac0eed0c8b1b4`
- Run outputs were copied into `run1/` and `run2/` immediately after
  each run (snapshots in the work dir are authoritative).

## Repo

- Local git commit: `d2a2cd411849cdd1dfb1ad09e7e11865dd1bb41d`
  ("The Moon Finally Answers Back — one-line comeback")
- Files: `main.py`, `README.md` (3 make.fun badges, repo
  `makefun-u-mang-the-moon-finally-answers-back-781a7ec1`, bounty page
  `https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1`,
  `ref=susay21` footer), `LICENSE` (MIT, SPDX-License-Identifier: MIT
  line), `.gitignore`, `run1/entry.txt`, `run2/entry.txt`.
- The GitHub repo under `shusay12` has NOT been created yet (that step
  belongs to submission, via the cloud browser, byte-identical files).

## Blocked steps — execution-risk check

After the local `git init` + commit completed, the system flagged that
step's result with an execution-risk check: the repo content can run
code during ordinary processing (git hooks), and the notice prohibits
running, cloning, checking out, extracting, building, testing,
importing, loading or sourcing that content, and running git commands
inside it. Per the task's hard rules the following steps were STOPPED
immediately and NOT retried:

1. **Bundle build** (NOT RUN) — the intended command was:
   `node <kit>/cli/makefun.mjs bundle --repo
   ~/workspace/makefun/u-mang-the-moon-finally-answers-back-781a7ec1
   --out <bundle>.tar.gz --session <explicit session flags>
   --no-discover --prompt-origin scheduled --prompt-via "scheduled cron
   makefun-new-bounty-watch" --prompt-file
   /home/hatch/workspace/goals/make-fun-free-bounty-entries/hidden_files/prompt-20261125-1350.txt
   --muse-usage <file> --mcp none --harness muse --model muse-spark-1.3
   --provider meta --effort default`
   No bundle exists; no bundle sha256 to report.
2. **Kit check** (NOT RUN) — `makefun check --kit <kit dir> --repo
   <work dir> --transcripts <bundle>` requires the bundle; no pass/fail
   counts to report. Target was 14 passed / 0 failed.

## Usage rows

Not queried: the bundle step was blocked before any usage file was
needed. The parent re-bundles with `--muse-usage` when the rows exist;
expect `thinking_priced` to fail with 0 usage rows, as in recent
one-line entries.

## What remains undone (for the parent)

- Create the GitHub repo `shusay12/makefun-u-mang-the-moon-finally-answers-back-781a7ec1`
  (cloud browser, byte-identical files) — not attempted here.
- Build the transcript bundle with the flags above (needs the
  execution-risk question resolved: the user should be asked in plain
  words whether to go ahead processing the flagged repo content).
- Run `makefun check` on the bundle; target 14 passed / 0 failed.
- Submit via `~/workspace/makefun/agent/submit.mjs` (or the kit's submit
  route) and record the submission id + stage in
  `~/workspace/makefun/STRATEGY-LEDGER.md`.
- Nothing was submitted; no submission id exists yet. No wallet signing,
  no payments, no network calls from the entry program. `~/.makefun/credentials`
  was never moved, replaced, printed, or read.
