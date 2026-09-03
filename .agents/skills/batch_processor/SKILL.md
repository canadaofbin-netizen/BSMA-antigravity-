---
name: batch_processor
description: Master orchestrator loop for automating the pure data extraction of included academic papers.
---

# Batch Processor Loop (Data Extraction Engine)

When the user asks you to "run the batch processor" or "extract data from papers", you must act as the Master Orchestrator and follow this precise Loop logic:

## 1. Queue Self-Healing & Retrieval (Stateful Poison Pill Defense)
- **Self-Healing:** Before starting, read `batch_queue.csv` (or `scratch/batch_queue.csv`). If any papers are stuck in `PROCESSING` status, increment their `ROLLBACK_COUNT` column by 1 and auto-rollback their status to `PENDING`. 
- **Max 2 Rollbacks (Poison Pill):** If a paper's `ROLLBACK_COUNT` exceeds 2, DO NOT rollback to `PENDING`. Immediately mark it as `PERMANENT_FAIL` to prevent an infinite crash loop.
- Identify the next `PENDING` paper(s) to process where the initial screening status is `1 = Include`.
- Change their status to `PROCESSING` in the CSV immediately.

## 2. 4-Node Multi-Agent Extraction (Per Paper)
For each paper in the batch, you must coordinate 4 distinct Nodes:
- Run `python .agents/scripts/find_pdf.py --id [Article_ID]` to automatically locate the `.txt` file.
- **Node 1 (Pre-flight Triage):** Spawn a subagent to scan for Time-lag/Longitudinal flags.
- **Node 2 (Footnote Scanner):** Spawn a subagent to check Table notes for partial correlations/controls.
- **Node 3 (Table Parser):** Spawn a subagent to extract the correlation matrix using CoT matrix reasoning.
- **Node 4 (Text Analyzer):** Spawn a subagent to extract verbatim sentences and dataset fingerprints.
- Await all nodes. Merge their outputs into a single JSON response.

## 3. Fast-Fail Pre-Check (CRITICAL)
- **Fast-Fail (Fatal Errors):** Before validation, check the merged string for fatal codes: `[DATA_NOT_FOUND]`, `[UNPARSEABLE_PDF]`, `[LoA_VIOLATION]`, `[CONSTRUCT_HOMONYMY_VIOLATION]`, `[PARTIAL_CORRELATION_POISONING]`, or `[AMBIGUOUS_MATRIX_DIAGONAL]`. 
- If ANY of these codes exist, DO NOT pass to Validator. Abort extraction immediately. Mark as `PERMANENT_FAIL` in `batch_queue.csv` and append the reason to `04_Reports/error_report.md`.

## 4. Extraction Validation Chaining
- Cross-check the Merged JSON payload and the original Correlation Table against the strict fidelity and reliability rules in `extract_measures/SKILL.md`.
- If verification returns `PASS`, proceed to step 5.
- If verification returns `REJECT_RETRY`, retry up to 3 times. 
- If verification returns `FATAL_REJECT`, treat it as a Fast-Fail (Abort immediately, mark as `PERMANENT_FAIL`).

## 5. 4-Sheet Excel Routing & Atomic Sync
- **Excel Injection (Safe CLI Args):** ONLY if validation passed, save the merged JSON payload to a temporary file (e.g., `temp_payload.json`). Invoke `python .agents/scripts/universal_excel_inserter.py --excel 03_Coding_Sheets/BSMA_Master_Coding_Sheet.xlsx --data-file temp_payload.json`. The script will handle routing to Raw, Transformed, Imputed, or Salami sheets.
- **Atomic Sync:** The moment a paper succeeds or fails, immediately update its status and `ROLLBACK_COUNT` in `batch_queue.csv` and execute `git add .`, `git commit -m "Auto-extracted measures for [Paper ID]"`, and `git push` to save progress atomically.

## 6. Reporting
- Present a summary of the batch run to the user. Provide a link to the `error_log.md` if any failed.
