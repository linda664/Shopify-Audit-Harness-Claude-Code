---
name: write
description: Phase 3 of the Qosmic audit. Write the final report.
---

# Write

## Goal
Produce one audit report file at `sample_output/<domain>.md` that matches the bar of `target_report.md`.

## Report structure

### 1. Executive summary
- 2-3 paragraphs of prose
- Paragraph 1: biggest single leak — what's costing the store the most right now
- Paragraph 2: the 2-3 compounding problems around it
- Paragraph 3: what to fix first and why
- Tone: direct, specific, clear, no fluff. Read target_report.md for the voice.

### 2. Proposed experiments (10 total)
For each experiment use this exact format:

exp-[id] — [Title]
Pillar: [Conversion / AOV / Retention / Acquisition / Performance]
Affected surface: [component or page name]
URL: [full URL]
Evidence: [URL or screenshot path — must be specific]
Hypothesis: [CVR/AOV/metric improves by X because evidence shows Y]
Primary change: [one concrete thing to ship]
Primary KPI: [one metric]
Decision rule: [Ship if X improves without hurting Y]
Expected lift: [+X–Y%]
Confidence: [Z%]

### 3. Competitor analysis
Markdown table with columns:
| Competitor | Domain | Positioning | What they make easier | [Store] edge | Pattern to adapt |

### 4. Technical checks
Markdown table with columns:
| Check | Status | Detail |

Status must be one of: Pass / Warn / Fail
Include all 15 checks from skills/crawl.md

## Quality check before saving

- [ ] Executive summary is 2-3 paragraphs, no bullet points
- [ ] Exactly 10 experiments
- [ ] All 5 pillars covered
- [ ] Every experiment has evidence cited (URL or path)
- [ ] Competitor table has 3-4 rows
- [ ] Technical checks table has ~15 rows
- [ ] File saved to `sample_output/<domain>.md`

## Done
Report is complete. Do not add commentary after the report.

