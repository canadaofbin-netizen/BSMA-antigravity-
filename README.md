# BSMA: Boundary Spanning Meta-Analysis

> Systematic meta-analysis project on the antecedents and outcomes of Individual-level Boundary Spanning Behavior (BSB)

---

## Project Overview

This project conducts a comprehensive meta-analysis of individual-level Boundary Spanning Behavior (BSB) across intra- and inter-organizational boundaries. Targeting 701 academic papers, it utilizes an AI-assisted screening pipeline alongside manual coding to perform Include/Exclude judgments and extract effect sizes.

---

## Directory Structure

```
BSMA ANTIGRAVITY/
├── 01_Academic_Papers/              701 PDFs (Strict naming: [ID] Author (Year) - Title.pdf)
├── 02_Reference_Manuals/            Coding manuals and reference documents
├── 03_Validation_Results/           AI validation result Excel files
│   ├── BSMA_AI_Run_V1_AggRecovery.xlsx   V1: 115 Include / 586 Exclude
│   └── BSMA_AI_Run_V2_Broad.xlsx         V2: Broad rules (TBD)
├── 04_Reports/                      Analysis reports (Match Rate, Screening Report)
├── 99_Archives_and_Backups/         Backups and legacy files
│   ├── NEVER_CHANGE_IN_ANY_CASES/   Immutable master backup (STRICTLY NO MODIFICATIONS)
│   ├── Database_Milestones/         DB snapshots
│   ├── Prompt_Freezes/              Pipeline rule snapshots
│   ├── LLM_Audit_Trails/            AI audit logs
│   ├── Cleanup_Logs/                Cleanup operation logs
│   └── Legacy/                      Legacy code and rules
├── .agents/                         AI agent settings and skills
│   ├── AGENTS.md                    Global rules (SSOT)
│   └── skills/                      Module-specific skill definitions
├── scratch/                         Temporary workspace (.gitignore)
│   ├── extracted_texts/             PDF extracted texts (reusable)
│   ├── ocr_images/                  OCR page images
│   └── _disposable/                 Disposable scripts/intermediate results
├── BSMA_Master_Coding_Sheet.xlsx    Master coding sheet (50 columns, based on V1)
├── CHANGELOG.md                     Rule change history
└── memory.md                        AI working memory and precedents
```

---

## Validation Versions

| Version | File Name | Include | Exclude | Rule Characteristics |
|---|---|---|---|---|
| **V1** (=V8) | `BSMA_AI_Run_V1_AggRecovery.xlsx` | 115 | 586 | Strict + Aggregation Recovery |
| **V2** (=V9) | `BSMA_AI_Run_V2_Broad.xlsx` | TBD | TBD | Broad (Researcher Decision 2026-07-28) |

For detailed rule changes, please refer to [CHANGELOG.md](CHANGELOG.md).

---

## Branch Strategy

| Branch | Rules | Role |
|---|---|---|
| `main` | 🔒 V1 Strict | **Base branch.** Currently finalized V1 rules + Master data. Starting point for all work |
| `strict-include-exclude-rules` | 🔒 V1 Strict | **main snapshot (locked).** For immutable preservation of V1 Strict rules. Do not modify |
| `develop` | 🔓 V2 Broad | **Working branch.** Used for experiments/development with V2 Broad rules |
| `loose-include-exclude-rules` | 🔓 V2 Broad | **V2 snapshot (locked).** For immutable preservation of V2 Broad rules. Do not modify |
| `feature/strict-pipeline` | 🔓 V2 Broad | **Feature development.** Used for adding/modifying pipeline features |
| `experiment/v9-comparison` | 🔓 V2 Broad | **Experimental.** V1/V2 comparative analysis, A/B testing, etc. |

```
main (V1 Strict) ----> strict-include-exclude-rules (Locked copy)
  └----> develop (V2 Broad) ----> loose-include-exclude-rules (Locked copy)
                             ----> feature/strict-pipeline (Feature dev)
                             ----> experiment/v9-comparison (Experiment)
```

**The only difference between `main` and the other branches is 2 Include/Exclude rule files:**
- `screening_rules_core.md`
- `screening_edge_cases.md`

### Frozen Tags
- `v1-strict-rules-frozen`: V1 Strict rule immutable snapshot
- `v2-broad-rules-frozen`: V2 Broad rule immutable snapshot

---

## AI Pipeline

### Include/Exclude Screening
Processes 701 papers in parallel using the AI-based automated screening pipeline.

**Usage:**
- `/includeexclude` - Execute automated screening pipeline
- `/workspace_lint` - Workspace hygiene check
- `/ask [question]` - Read-only Q&A (No file modifications)

### Core Rules
1. **Zero Guesswork Policy**: Numeric missing = `999`, Text missing = `"Not Reported"`
2. **Verbatim Quote**: Verbatim quotes are mandatory for all judgments (Col 16)
3. **Immutable Vault**: `NEVER_CHANGE_IN_ANY_CASES/` strictly prohibits modifications
4. **SSOT**: `AGENTS.md` is the only source of truth for rules

---

## Key Files

| File | Purpose |
|---|---|
| `BSMA_Master_Coding_Sheet.xlsx` | Master coding sheet (50 columns, based on V1) |
| `.agents/AGENTS.md` | AI agent global rules |
| `CHANGELOG.md` | V1/V2 rule change history |
| `memory.md` | AI working memory and precedent records |

---

## Quick Start

```bash
# Check current branch
git branch --list

# Check rule differences between V1 vs V2
git diff main develop -- .agents/skills/include_exclude_pipeline/references/

# Execute screening pipeline (in Antigravity IDE)
/includeexclude

# Workspace check
/workspace_lint
```
