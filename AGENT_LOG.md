# AGENT_LOG.md

## Time breakdown

| Part | Time spent |
|---|---|
| Understand task and figure out the case structure | ~50 min |
| Part 1 — Runtime harness (CLAUDE.md + skills/) | ~45 min |
| Part 2 — Eval system (eval.py + EVAL_LOOP.md) | ~45 min |
| WORKFLOWS.md + AGENT_LOG.md | ~30 min |
| Loom recording | ~40 min |
| **Total** | **~3.50 hrs** |

---

## Part 1 — Runtime harness

### Prompts I fed the agent

1. "Help me design a CLAUDE.md entry point that turns Claude Code into a Shopify CRO audit agent. The agent takes a single URL as input and outputs a structured report matching this format: [pasted target_report.md structure]"

2. "Write a crawl skill file (skills/crawl.md) with YAML frontmatter. It should tell the agent exactly which pages to visit on any Shopify store, what to capture on each page, and how to run 15 standard technical checks."

3. "Write a reason skill file (skills/reason.md). It should guide the agent to identify revenue leaks across 5 pillars (Conversion, AOV, Retention, Acquisition, Performance) and construct 10 experiments each with hypothesis, evidence citation, KPI, and decision rule."

4. "Write a write skill file (skills/write.md). It should produce a report matching target_report.md — executive summary, 10 experiments, competitor table, technical checks table."

5. "Audit this Shopify store: https://gingerpeople.com"

6. "Audit this Shopify store: https://zenrojas.com"

### Agent drove
- All three skill file drafts (crawl, reason, write)
- Both full audit reports (gingerpeople, zenrojas)
- Crawling, competitor research, technical checks

### I took the wheel
- Reviewed target_report.md to calibrate quality bar before writing any skill
- Restructured crawl.md after first draft was too vague on evidence citation
- Verified zenrojas output manually (checked cart, FAQ 404, shipping threshold) and found an agent error — stale cart bug
---

## Part 2 — Eval system

### Prompts I fed the agent

1. "Write a Python eval script (evals/eval.py) that scores any Shopify audit report against a rubric without needing a reference report. Score four sections: executive summary, experiments, competitor analysis, technical checks. Output total score and per-section notes."

2. "Run the eval against sample_output/gingerpeople.com.md"

3. "Run the eval against sample_output/zenrojas.com.md"

### Agent drove
- Full eval.py implementation
- Regex parsing for all four sections
- Score breakdown and notes output

### I took the wheel
- Designed the rubric dimensions before asking agent to implement
- Identified three eval failure modes from manual zenrojas review (out-of-stock issues, free shopping fee inconsistency, stale cart bug) and wrote those into EVAL_LOOP.md myself
- Wrote the month 1-3 autonomy roadmap in EVAL_LOOP.md — agent drafted, I rewrote substantially