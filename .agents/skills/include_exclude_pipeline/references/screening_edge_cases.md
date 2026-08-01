# Screening Edge Cases Reference

> **Note:** This file is an ON-DEMAND reference meant to supplement the core screening rules found in `screening_rules_core.md`. Use this document when encountering ambiguous cases.

## Trap Warning Quick-Reference Index

| Trap | Parent Rule (Tier) | Action |
|---|---|---|
| 1:1 Matched Dyad Safe Harbor | Rule 4 (Tier 2) | Do NOT apply Code 3 |
| AI Tool Interaction | Rule 4 (Tier 2) | Exclude — Code 1 |
| SEM-only Data Warning | Rule 7 (Tier 0) | Exclude — Code 1 |
| Implanted Boundary Spanner | Rule 2 (Tier 1) | INCLUDE |
| Leader BSB Trap (Blau's index) | Rule 1 (Tier 1) | Exclude — Code 1 & 3 |
| N=Leaders=N=Teams | Rule 1 (Tier 1) | INCLUDE (if not aggregated) |
| Individual-Measurement Aggregation Recovery | Rule 4 (Tier 2) | INCLUDE (unconditional) |
| Work-related Communication Frequency | Rule 6 (Tier 2) | INCLUDE (if cross-boundary) |
| All Network Structural Metrics | Rule 6 (Tier 2) | INCLUDE (Burt, ERGM, E-I, betweenness, etc.) |

## Detailed Edge Case Explanations

### 1:1 Matched Dyad Safe Harbor
If a study uses 1-to-1 matched pairs (e.g., 1 expatriate paired with exactly 1 coworker) and each individual appears only once in the dataset, statistical independence IS preserved. Do NOT apply Code 3. Only apply Code 3 when N = relationships (e.g., 87 individuals generating 673 dyadic ties).

### AI Tool Interaction Exclusion
BSB must be an interpersonal, human-to-human behavior. If the "boundary spanning" measured involves using Generative AI tools (e.g., ChatGPT) to gather information, this is human-computer interaction and lacks BSB construct validity → Exclude under Code 1.

### SEM-only Data Warning
If a paper relies entirely on SEM path coefficients and does NOT provide a zero-order correlation matrix (even latent), it must be excluded for lacking extractable effect sizes. Do NOT confuse partial rectangular cross-correlation tables with full square correlation matrices.

### Implanted Boundary Spanner / Knowledge Exchange
If a study's sample consists of employees whose job role is boundary spanning (e.g., logistics implants on-site at client facilities, expatriates) AND the study measures their knowledge exchange, coordination, or information-sharing behavior with the partner organization, this IS a valid BSB construct → INCLUDE. Do NOT exclude just because the paper labels it "knowledge exchange" instead of "boundary spanning behavior".

### Leader BSB Trap (Blau's index)
Do NOT be fooled by the label "Boundary-spanning leadership". If the items measure internal demographic diversity management (e.g., bridging age gaps within a branch using Blau's index), it is inclusive leadership, NOT structural BSB → Exclude under Code 1 & 3.

### N=Leaders=N=Teams Exception & Aggregation Guardrail
When exactly one leader exists per team, the effective N for measuring the leader's BSB is N_leaders. However, this exception ONLY applies if the final statistical analysis (e.g., zero-order correlation matrix) preserves the individual-level unit of analysis. If the leader's data is aggregated into a team-level score, or if the entire analytical model is conducted at the macro team-level (e.g., predicting team-level performance with N_teams), the study MUST be excluded under Code 3. Do not apply this exception to aggregated team-level models.

### Time Allocation Trap (SUPERSEDED)
**[Researcher Decision 2026-07-28]** This trap has been relaxed. If the study measures the percentage of time an employee spends interacting with external parties (customers, other departments, etc.) in a work-related context, this IS a valid BSB operationalization → INCLUDE. Only non-work time allocation (e.g., personal social time) remains invalid.

### PLS-SEM Dyadic Trap
If a study uses PLS-SEM with degree-symmetric dyadic consensus variables where N = relationships (not individuals), it violates statistical independence → Exclude under Code 3. Also watch for nested data (e.g., N=158 managers in 58 projects) where project-level outcomes are duplicated.

### CEO BSB Exception
If a CEO rates their OWN individual boundary spanning behavior using "I" referent items (e.g., "I solicit information from external channels") and N=firms=N=CEOs (one respondent per firm), this is valid individual-level BSB → INCLUDE. Do not confuse with firm-level alliance studies.

### Network-Based BSB Inclusion (EXPANDED)
**[Researcher Decision 2026-07-28]** ALL network-based measures of cross-boundary interaction ARE valid BSB proxies and MUST BE INCLUDED. This includes: (a) Advice-seeking network degree centrality, (b) E-I index, (c) Ego-network heterogeneity, (d) Burt's structural constraint/structural holes, (e) Sociometric sensor data (work-related speaking events), (f) ERGM parameters, (g) Betweenness centrality and brokerage measures. Do NOT exclude simply because BSB is measured via SNA rather than a Likert scale.

### Rule 5 vs Rule 6 Edge Case (Cross-Departmental Communication) (SUPERSEDED)
**[Researcher Decision 2026-07-28]** Cross-departmental work-related communication frequency (e.g., how often employees discuss work-related issues with members of other departments) IS a valid BSB operationalization → INCLUDE. Only purely non-work social communication without any boundary-spanning work context should be excluded.

### Individual-Measurement Aggregation Recovery (UNCONDITIONAL)
**[Researcher Decision 2026-07-28]** If a study collected individual-level BSB responses (using "I" referent items) but aggregated them to team/dyad level for analysis, it MUST be coded as `1 = Include` **unconditionally**. The previous "author contact required" qualifier has been removed.

Key verification checklist:
1. ✅ Survey items use "I" / "My" referent (individual-level measurement)
2. ✅ Notes confirm individual-level data collection occurred before aggregation
3. ❌ Does NOT apply if items use "The team" / "We" / "Our firm" referent (referent-shift)
4. ❌ Does NOT apply if measurement was designed as team-level from the start

Canonical examples:
- BSMA0385: Individual respondents rated BSB frequency → averaged to team level (N=23 teams)
- BSMA0413: Individual employees surveyed (N=457) → aggregated to unit-dyad level (N=462 dyads)
