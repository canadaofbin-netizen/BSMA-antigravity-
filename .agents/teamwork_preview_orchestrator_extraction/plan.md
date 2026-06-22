# Plan: Meta-Analytic Data Extraction and Shadow Report Generation

## Objective
Coordinate the parallel extraction of meta-analytic data from Marrone 2007, Liu 2024, and Akaho 2024, and generate three compliant Shadow Reports under `BSMA ANTIGRAVITY/03_Shadow_Reports/`.

## Complexity Assessment
- **Scope**: Multi-file data extraction from academic PDFs.
- **Knowledge**: Requires strict compliance with the project's Coding Rulebook (e.g., Zero Guesswork Policy, demographic formatting, no bold headers in data tables, coding categorical variables, etc.).
- **Risk**: Low risk of breaking code (mostly data generation), but high precision required for data integrity.
- **Ambiguity**: Low. Files to read and write are explicitly named.

## Steps

### Step 1: Project Setup
- Define the global milestones and code/document layout in `PROJECT.md`.
- Read and understand the specific details of the Coding Rulebook (`05_Coding_Rulebook/`).

### Step 2: Extract & Generate Shadow Report for Marrone 2007
- Spawn a `teamwork_preview_explorer` to analyze the PDF `[18] Marrone Jennifer A., Tesluk Paul E., Carson Jay B. (2007) A Multilevel Investigation of Antecedents and Consequences of Team Member Boundary-Spanning Behavior.pdf`.
- Collect the explorer report detailing all correlations, demographics, and scales used.
- Spawn a `teamwork_preview_worker` to write the shadow report `03_Shadow_Reports/Marrone_2007_Shadow_Report.md` following the data tables schema, ensuring no bold text in headers.

### Step 3: Extract & Generate Shadow Report for Liu 2024
- Spawn a `teamwork_preview_explorer` to analyze `[256] Liu Ting et al. (2024) Expatriates' boundary-spanning double-edged effects in multinational enterprises.pdf`.
- Collect findings.
- Spawn a `teamwork_preview_worker` to write `03_Shadow_Reports/Liu_2024_Shadow_Report.md`.

### Step 4: Extract & Generate Shadow Report for Akaho 2024
- Spawn a `teamwork_preview_explorer` to analyze `[166] Akaho Yuma (2024) Conceptualizing the adventure tourist as a cross-boundary learner.pdf`.
- Collect findings.
- Spawn a `teamwork_preview_worker` to write `03_Shadow_Reports/Akaho_2024_Shadow_Report.md`.

### Step 5: Verification & Review
- Verify that the generated reports contain the required tables (Effect Size ID, N, Means, SDs, r, etc.).
- Verify that table headers are NOT bolded (e.g., `| Effect Size ID | N |` instead of `| **Effect Size ID** | **N** |`).
- Verify adherence to the Coding Rulebook (e.g., `999` for missing/inapplicable values, specific copy-pasted measure text, KY as coder, sequential Article IDs, etc.).
- Check inclusion/exclusion judgments (Akaho 2024 is likely excluded as a theoretical paper, but we still write its report).

### Step 6: Completion & Reporting
- Deliver final status to the parent agent.
