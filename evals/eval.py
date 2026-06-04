#!/usr/bin/env python3
"""
Qosmic Audit Eval System
Scores any audit report against a rubric — no human needed.
"""

import re
import sys
from pathlib import Path


def load_report(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def score_executive_summary(report: str) -> dict:
    """Check executive summary exists and has 2-3 paragraphs of prose."""
    score = 0
    notes = []

    # Find executive summary section
    match = re.search(r"## Executive summary(.*?)## Proposed experiments", report, re.DOTALL)
    if not match:
        return {"score": 0, "max": 20, "notes": ["Executive summary section missing"]}

    content = match.group(1).strip()
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip() and not p.startswith("#")]

    if len(paragraphs) >= 2:
        score += 10
    else:
        notes.append(f"Expected 2-3 paragraphs, found {len(paragraphs)}")

    # Check for specificity (numbers, URLs, named evidence)
    has_numbers = bool(re.search(r"\d+", content))
    has_urls = bool(re.search(r"https?://", content))
    if has_numbers:
        score += 5
    else:
        notes.append("Executive summary lacks specific numbers")
    if has_urls:
        score += 5
    else:
        notes.append("Executive summary lacks URL citations")

    return {"score": score, "max": 20, "notes": notes}


def score_experiments(report: str) -> dict:
    """Check 10 experiments spanning all 5 pillars with evidence."""
    score = 0
    notes = []

    # Find experiments section
    match = re.search(r"## Proposed experiments(.*?)## Competitor analysis", report, re.DOTALL)
    if not match:
        return {"score": 0, "max": 35, "notes": ["Proposed experiments section missing"]}

    content = match.group(1)

    # Count experiments
    exp_count = len(re.findall(r"### exp-", content))
    if exp_count == 10:
        score += 10
    elif exp_count >= 8:
        score += 6
        notes.append(f"Expected 10 experiments, found {exp_count}")
    else:
        notes.append(f"Too few experiments: {exp_count}")

    # Check all 5 pillars covered
    pillars = ["Conversion", "AOV", "Retention", "Acquisition", "Performance"]
    found_pillars = []
    for pillar in pillars:
        if pillar in content:
            found_pillars.append(pillar)

    pillar_score = len(found_pillars) * 3
    score += pillar_score
    missing = set(pillars) - set(found_pillars)
    if missing:
        notes.append(f"Missing pillars: {missing}")

    # Check evidence citations (URLs) in experiments
    exp_blocks = re.findall(r"### exp-.*?(?=### exp-|## Competitor)", content, re.DOTALL)
    cited = sum(1 for b in exp_blocks if re.search(r"https?://", b))
    if cited == len(exp_blocks):
        score += 10
    else:
        score += int(10 * cited / max(len(exp_blocks), 1))
        notes.append(f"Only {cited}/{len(exp_blocks)} experiments have URL evidence")

    return {"score": min(score, 35), "max": 35, "notes": notes}


def score_competitor_analysis(report: str) -> dict:
    """Check competitor table has 3-4 rows with substance."""
    score = 0
    notes = []

    match = re.search(r"## Competitor analysis(.*?)## Technical checks", report, re.DOTALL)
    if not match:
        return {"score": 0, "max": 20, "notes": ["Competitor analysis section missing"]}

    content = match.group(1)

    # Count table rows (non-header)
    rows = [l for l in content.split("\n") if l.startswith("|") and "---" not in l and "Competitor" not in l and l.strip() != "|"]
    row_count = len(rows)

    if row_count >= 3:
        score += 10
    else:
        notes.append(f"Expected 3-4 competitor rows, found {row_count}")

    # Check for domains in table
    domains = re.findall(r"\b\w+\.\w{2,}\b", content)
    if len(domains) >= 3:
        score += 5
    else:
        notes.append("Competitor domains not clearly listed")

    # Check for "Pattern to adapt" or actionable column
    if "adapt" in content.lower() or "pattern" in content.lower():
        score += 5
    else:
        notes.append("Missing actionable 'Pattern to adapt' column")

    return {"score": score, "max": 20, "notes": notes}


def score_technical_checks(report: str) -> dict:
    """Check technical checks table has ~15 rows with Pass/Warn/Fail."""
    score = 0
    notes = []

    match = re.search(r"## Technical checks(.*?)$", report, re.DOTALL)
    if not match:
        return {"score": 0, "max": 25, "notes": ["Technical checks section missing"]}

    content = match.group(1)

    # Count rows
    rows = [l for l in content.split("\n") if l.startswith("|") and "---" not in l and "Check" not in l]
    row_count = len(rows)

    if row_count >= 14:
        score += 10
    elif row_count >= 10:
        score += 6
        notes.append(f"Expected ~15 checks, found {row_count}")
    else:
        notes.append(f"Too few technical checks: {row_count}")

    # Check Pass/Warn/Fail present
    statuses = {"Pass": 0, "Warn": 0, "Fail": 0}
    for status in statuses:
        statuses[status] = content.count(status)

    if all(v > 0 for v in statuses.values()):
        score += 10
    elif sum(1 for v in statuses.values() if v > 0) >= 2:
        score += 5
        notes.append("Not all three statuses (Pass/Warn/Fail) present")

    # Check for specific detail per row
    rows_with_detail = sum(1 for r in rows if len(r.split("|")) >= 3 and r.split("|")[2].strip())
    if rows_with_detail >= 12:
        score += 5
    else:
        notes.append(f"Only {rows_with_detail} rows have detail notes")

    return {"score": score, "max": 25, "notes": notes}


def eval_report(path: str) -> dict:
    report = load_report(path)

    results = {
        "executive_summary": score_executive_summary(report),
        "experiments": score_experiments(report),
        "competitor_analysis": score_competitor_analysis(report),
        "technical_checks": score_technical_checks(report),
    }

    total = sum(r["score"] for r in results.values())
    max_total = sum(r["max"] for r in results.values())

    return {
        "file": path,
        "total": total,
        "max": max_total,
        "pct": round(100 * total / max_total),
        "sections": results,
    }


def print_results(result: dict):
    print(f"\n{'='*50}")
    print(f"AUDIT EVAL: {result['file']}")
    print(f"TOTAL: {result['total']}/{result['max']} ({result['pct']}%)")
    print(f"{'='*50}")

    for section, data in result["sections"].items():
        status = "✓" if data["score"] == data["max"] else "~" if data["score"] > 0 else "✗"
        print(f"\n{status} {section.upper()}: {data['score']}/{data['max']}")
        for note in data["notes"]:
            print(f"  - {note}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python eval.py <report.md>")
        sys.exit(1)

    result = eval_report(sys.argv[1])
    print_results(result)
    sys.exit(0 if result["pct"] >= 70 else 1)