# Rule: Excel Coding Sheet Data Integrity

This document defines the strict data type policies, template schemas, and evidence standards for all BSMA coding sheets.

---

## 1. Universal Zero Guesswork Policy (Rule 1)
- **Absolute Prohibition on Imputation:** Never guess or impute data.
- **Type-Safe Missing Values:**
  - If a numeric value is missing or not reported, YOU MUST return the integer `999`.
  - If a string/text field is missing or not reported, YOU MUST return the string `"Not Reported"`.
- **No Averaging / Deduction:** Do NOT calculate averages or deduce missing values under any circumstances.

---

## 2. Template Structure & Format Compliance (Rules 3, 6, 19)
- **Universal Master Insertion (Rule 6):** ALL successfully processed papers MUST be injected into `03_Coding_Sheets/BSMA_Master_Coding_Sheet.xlsx`. Every paper must retain its assigned BSMA ID.
- **50-Column Full Extraction Schema (Rule 19):** `03_Coding_Sheets/BSMA_Master_Coding_Sheet.xlsx` is the ultimate master template and contains the 50-column "Full Text Data Extraction" structure (Columns A through AX, covering Study/Sample Descriptors and Measure Descriptors).
- **Screening vs Extraction Separation (Rule 19):** `03_Coding_Sheets/BSMA_Master_Coding_Sheet.xlsx` contains the full 50-column extraction schema (Col A through AX). Dedicated screening views or test sheets retain only Columns A through P (ID, Judgments, Reasons, Abstract, Title, Notes) to separate high-level screening from full-text data extraction.
- **Prohibition of Bold Headers (Rule 3):** Never use markdown bold (`**`) or rich text bolding inside Excel header cells.

---

## 3. Verbatim Quote Evidence Standards (Rule 13)
- **Mandatory Quote Injection:** Whenever a paper is judged—whether `1 = Include` or `0 = Exclude`—you MUST extract and inject exact, character-for-character verbatim quotes from the PDF text into Col 16 (Notes).
- **Strict Prohibition of Ellipses (No Truncation):** NEVER use ellipses (`...`) to summarize, abbreviate, or truncate sentences. You must extract full, complete sentences or paragraphs exactly as they appear in the original text.
- **Maximum Multi-Section Evidence:** Collect the maximum evidence possible from multiple sections (Abstract, Participants, Measures, Discussion) to robustly prove the sample type or exclusion reason.
- **Exact Note Format:** Use brackets to indicate the section of each quote:  
  `[Reason summary]. Verbatim Evidence: "[Section 1] <exact quote 1>" [Section 2] "<exact quote 2>"`
