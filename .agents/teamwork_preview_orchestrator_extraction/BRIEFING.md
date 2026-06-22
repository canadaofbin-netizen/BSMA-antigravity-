# BRIEFING — 2026-06-19T23:30:00+01:00

## Mission
Coordinate the parallel extraction of meta-analytic data from Marrone 2007, Liu 2024, and Akaho 2024, writing shadow reports for each to `03_Shadow_Reports/`.

## 🔒 My Identity
- Archetype: Project Orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\.agents\teamwork_preview_orchestrator_extraction
- Original parent: main agent
- Original parent conversation ID: 537a84fc-1c67-4d55-aa61-fc04e6b211c4

## 🔒 My Workflow
- **Pattern**: Project
- **Scope document**: g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\.agents\teamwork_preview_orchestrator_extraction\PROJECT.md
1. **Decompose**: Decompose the task into three papers and parallel data extraction.
2. **Dispatch & Execute**:
   - **Delegate**: Spawn parallel explorers / workers for each academic paper.
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: Self-succeed at 16 spawns.
- **Work items**:
  1. Write plan to plan.md [pending]
  2. Setup PROJECT.md [pending]
  3. Extract Marrone 2007 [pending]
  4. Extract Liu 2024 [pending]
  5. Extract Akaho 2024 [pending]
  6. Verify all shadow reports [pending]
- **Current phase**: 1
- **Current focus**: Setting up plans and projects.

## 🔒 Key Constraints
- Output three separate Markdown files in `BSMA ANTIGRAVITY/03_Shadow_Reports/`:
  - `Marrone_2007_Shadow_Report.md`
  - `Liu_2024_Shadow_Report.md`
  - `Akaho_2024_Shadow_Report.md`
- These files MUST contain the actual data tables with Effect Size ID, N, Means, SDs, r, etc.
- Do NOT use bold markdown (`**`) in the table headers.
- Enforce the Zero Guesswork Policy.
- Never reuse a subagent after it has delivered its handoff — always spawn fresh

## Current Parent
- Conversation ID: 537a84fc-1c67-4d55-aa61-fc04e6b211c4
- Updated: not yet

## Key Decisions Made
- Use teamwork_preview_explorer to investigate each paper.
- Use teamwork_preview_worker to write/edit each shadow report based on explorer analysis.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| Marrone Explorer | teamwork_preview_explorer | Extract Marrone 2007 paper | pending | 8b90e119-8dde-46d1-8bc4-7cbc1edc0190 |
| Liu Explorer | teamwork_preview_explorer | Extract Liu 2024 paper | pending | ddc433ff-7fb7-4983-afc0-97b7f7566fa2 |
| Akaho Explorer | teamwork_preview_explorer | Extract Akaho 2024 paper | pending | c81ef568-a348-4f1a-bf5f-52f4c20e0c01 |

## Succession Status
- Succession required: no
- Spawn count: 3 / 16
- Pending subagents: 8b90e119-8dde-46d1-8bc4-7cbc1edc0190, ddc433ff-7fb7-4983-afc0-97b7f7566fa2, c81ef568-a348-4f1a-bf5f-52f4c20e0c01
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: task-47
- Safety timer: none

## Artifact Index
- g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\.agents\teamwork_preview_orchestrator_extraction\plan.md — Orchestrator plan
- g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\.agents\teamwork_preview_orchestrator_extraction\progress.md — Progress tracker
- g:\My Drive\UCL\BSMA\BSMA ANTIGRAVITY\.agents\teamwork_preview_orchestrator_extraction\PROJECT.md — Project milestones
