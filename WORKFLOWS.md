# WORKFLOWS.md — How I work with coding agents day-to-day

## Tool stack

- **Claude Code** — primary coding agent for all implementation tasks
- **Claude.ai** — architecture discussions, prompt design, rubber-ducking hard problems
- **VS Code** — editor; Claude Code runs in integrated terminal
- **GitHub** — version control; agent commits directly to feature branches
- **Python + shell scripts** — glue layer for agent pipelines

## Delegation pattern

The core question I ask before every task: *can I write a contract for this?*
If I can specify inputs, outputs, and quality bar precisely — I delegate to the agent.
If the contract itself is the hard part — I do it myself first, then hand off execution.

**Agent drives:**
- Boilerplate and scaffolding (file structure, config, initial class stubs)
- Repetitive transformations (data cleaning, format conversion, test generation)
- First drafts of anything with a clear template (README, docstrings, SQL queries)
- Debugging with a clear error message and stack trace
- Implementing a spec I've already written

**I take the wheel:**
- Defining the architecture before any code is written
- Writing the prompt/skill/contract that the agent will execute against
- Reviewing agent output for logic errors, not syntax errors
- Any decision that touches system boundaries (auth, data model, external APIs)
- Knowing when to throw away agent output and start over

## Custom patterns I use

**Skill files over long prompts** — instead of writing a 500-word prompt every session,
I maintain skill files (like this harness) that encode the contract once and reuse it.
The agent reads the skill; I update the skill when output quality drifts.

**Agent log discipline** — I log every non-trivial prompt I give an agent and its output quality.
After 3–5 uses of the same pattern, I extract it into a reusable skill or slash command.

**Fail fast on ambiguity** — if the agent produces something clearly wrong in the first
10% of a task, I stop it immediately, tighten the contract, and restart.
Letting a bad direction run to completion wastes more time than the restart.

## Where I never fully delegate

- Security-sensitive code (auth flows, secrets handling)
- Data model migrations
- Anything that writes to production without a dry-run first
- Final review before a PR — I always read the diff myself