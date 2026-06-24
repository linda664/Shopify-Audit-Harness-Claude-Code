## Current state
The eval system (eval.py) scores audit reports against a rubric 
(coverage, specificity, actionability, [+ planned: citation 
reachability]). It is reference-free at runtime — it does not 
compare a new report against target_report.md, since no two 
Shopify stores share the same content, so direct comparison would 
answer the wrong question (similarity to one store ≠ quality).

target_report.md instead serves as a human calibration anchor, 
used outside the runtime loop: I judge a given report to be 
high-quality, save it as a known-good sample, and whenever I 
modify eval.py's scoring logic, I re-run the eval on this sample 
to check the score is still appropriately high. If it drops, that 
signals the scoring logic regressed — not that the report got 
worse — since I'm confident the content itself hasn't changed. 
Without this anchor, rubric drift could happen silently: I'd have 
no independent way to tell whether a scoring change made the 
system more accurate or just different.

Today, a human (me) also selects test URLs and reviews scores 
for sanity.

## Path to autonomy

**Step 1 — Self-sourcing test cases (weeks 1–2)**
Replace manual URL selection with a rotating pool of public 
Shopify stores, auto-flagging ones that produce unusually 
low/high scores or eval errors as the next calibration set.

**Step 2 — Automating the calibration check (weeks 3–6)**
Formalize the target_report.md check into a regression test that 
runs automatically whenever eval.py changes: re-score 
target_report.md (and a small growing set of other human-approved 
"known-good" reports) and flag if scores drift below a threshold. 
This turns what is currently a manual habit — rerun, eyeball the 
number — into a self-triggered check, so the system catches its 
own scoring drift without me remembering to test it.

**Step 3 — Closing the loop with the harness (months 2–3)**
Low-scoring dimensions get routed back as structured feedback into 
reason.md/write.md (e.g. "citation reachability scores low on X% 
of reports → tighten instruction to verify links before writing"). 
Eval output becomes harness input, not just a report card.

## What this looks like at 1–3 months
- New test stores are sampled automatically; humans see a weekly 
  digest, not individual runs.
- The known-good sample set (seeded by target_report.md) grows 
  over time as I approve more reports, giving the regression check 
  more coverage instead of relying on a single anchor.
- Rubric/eval logic changes are only flagged for human review when 
  the regression check fails — not on a fixed schedule.
- Harness prompt edits are proposed (diff + rationale) by the loop; 
  a human approves/rejects rather than writing them from scratch.

## Where humans stay in the loop — and why
- **Approving additions to the known-good sample set**: deciding 
  what counts as "a good audit" is a judgment call the system 
  shouldn't make about itself.
- **Approving harness prompt edits**: same reasoning — if the loop 
  could silently rewrite both the harness and the eval, regressions 
  in one could hide behind drift in the other.
- **Spot-checking the auto-sourced test pool**: to catch degenerate 
  cases (broken sites, non-Shopify false positives).

## Shrinking the surface over time
URL sourcing → autonomous first (low stakes, easy to sanity-check). 
Calibration regression-testing → autonomous once it's been run 
manually enough times to trust the threshold. Rubric edits and 
harness edits → stay human-gated, since they touch what 
"good" means and what the product actually outputs.