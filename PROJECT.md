# Project: Meta-Analytic Data Extraction (Marrone, Liu, Akaho)

## Architecture
- **Data Flow**: PDF papers (under `01_Academic_Papers/`) -> Information extraction by Explorers -> Shadow Report creation by Workers (under `03_Shadow_Reports/`) -> Verification.
- **Rulebook Guidelines**: Adhere to `05_Coding_Rulebook/` rules for table formatting, coding values, demographics, and exceptions.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Marrone 2007 | Extract meta-analytic correlations and demographics for Marrone (2007) and write Marrone_2007_Shadow_Report.md | None | IN_PROGRESS |
| 2 | Liu 2024 | Extract meta-analytic correlations and demographics for Liu (2024) and write Liu_2024_Shadow_Report.md | None | IN_PROGRESS |
| 3 | Akaho 2024 | Evaluate Akaho (2024) inclusion/exclusion, extract metadata, and write Akaho_2024_Shadow_Report.md | None | IN_PROGRESS |
| 4 | Verification | Review all 3 shadow reports to verify they adhere to the non-bold headers constraint and other coding rules | M1, M2, M3 | PLANNED |

## Interface Contracts
- **Shadow Report Schema**:
  - File format: Markdown
  - Directory: `03_Shadow_Reports/`
  - Name convention: `[Author]_[Year]_Shadow_Report.md`
  - Data table requirements: Must contain columns such as Effect Size ID, N, Means, SDs, r, etc., with NO bold text (`**`) in headers.
  - Inclusion/Exclusion Judgments: Coded as `1 = Include` or `0 = Exclude` as per rulebooks.
