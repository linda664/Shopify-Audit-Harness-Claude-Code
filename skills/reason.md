---
name: reason
description: Phase 2 of the Qosmic audit. Analyze crawl artifacts and identify revenue leaks.
---

# Reason

## Goal
Using your crawl artifacts, identify the top revenue leaks across all 5 pillars and construct 10 experiments.

## The 5 pillars

- **Conversion** — shoppers not completing purchase (unclear CTAs, broken paths, confusing navigation)
- **AOV** — missed upsell/bundle/cross-sell opportunities
- **Retention** — no repeat purchase hooks, no routines, no loyalty signals
- **Acquisition** — weak SEO landing pages, no use-case pages, missed high-intent traffic
- **Performance** — technical issues killing conversion (slow speed, 404s, broken checkout)

## For each experiment, construct

- **Title** — short, action-oriented
- **exp-id** — generate a random hex string like `exp-a1b2c3d4e5f6`
- **Pillar** — one of the 5 above
- **Affected surface** — which page or component
- **URL** — the specific page URL
- **Evidence** — cite the exact URL or crawl finding that supports this. Never speculate.
- **Hypothesis** — "CVR/AOV/retention improves by [doing X] because [evidence shows Y]"
- **Primary change** — one concrete thing to ship
- **Primary KPI** — one metric to measure
- **Decision rule** — "Ship if [KPI] improves without hurting [guardrail metric]"
- **Expected lift** — e.g. +10–18%
- **Confidence %** — your honest estimate (60–85% range typical)

## Rules

- Minimum 2 Conversion experiments
- Minimum 1 each: AOV, Retention, Acquisition, Performance
- Every experiment must cite specific evidence from your crawl
- No two experiments on the same page unless the changes are clearly distinct
- Rank by expected impact × confidence

## Competitor analysis

Identify 3-4 direct competitors by searching for the store's product category.
For each competitor record:
- Domain
- Positioning (1 sentence)
- What they make easier than the target store
- What the target store does better
- One pattern to adapt

## Output

When done reasoning, read `skills/write.md` and proceed.