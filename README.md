# shopify-audit-harness

A runtime harness that turns Claude Code into a Shopify CRO audit agent. Point it at any Shopify URL — it crawls the storefront, reasons over the artifacts, and produces a structured audit report.

## How it works

The harness follows three phases:

1. **Crawl** — visits key storefront surfaces (homepage, PDPs, cart, collections, FAQ, blog) and runs 15 standard technical checks
2. **Reason** — identifies revenue leaks across 5 pillars: Conversion, AOV, Retention, Acquisition, Performance
3. **Write** — produces a structured report with executive summary, 10 proposed experiments, competitor analysis, and technical checks table

## Usage

Open Claude Code in this directory and run:

The agent reads `CLAUDE.md` as its entry point and executes the three skill files in order.

## Eval system

`evals/eval.py` scores any audit report against a rubric without needing a reference report:

```bash
python evals/eval.py sample_output/gingerpeople.com.md
```

Scores four dimensions: executive summary, experiments, competitor analysis, technical checks. No ground truth required — the rubric generalizes to any Shopify store.

## Sample outputs

- `sample_output/gingerpeople.com.md` — calibration target (scored 95/100)
- `sample_output/zenrojas.com.md` — generalization target

## Structure

CLAUDE.md              # Agent entry point
skills/
crawl.md             # Phase 1: crawl instructions
reason.md            # Phase 2: reasoning framework
write.md             # Phase 3: report writing
evals/
eval.py              # Rubric-based eval scorer
sample_output/         # Generated audit reports
target_report.md       # Calibration anchor
EVAL_LOOP.md           # Autonomy roadmap for the eval system
AGENT_LOG.md           # Time log and prompt log
WORKFLOWS.md           # How I work with coding agents
