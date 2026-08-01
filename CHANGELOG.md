# BSMA Validation Rule Changelog

> Documents the rule changes between Validation versions and the resulting differences.

---

## Version Summary

| Version | File Name | Include | Exclude | Rule Characteristics |
|---|---|---|---|---|
| **V1** (=V8) | `BSMA_AI_Run_V1_AggRecovery.xlsx` | 115 | 586 | Strict + Aggregation Recovery |
| **V2** (=V9) | `BSMA_AI_Run_V2_Broad.xlsx` | TBD | TBD | Broad (Researcher Decision) |

---

## V1 -> V2: Addition of Aggregation Recovery Rule

**Git Commits:** `0820472` -> `da6da1a`  
**Result Change:** Include 106 -> 115 (+9 papers)

### Changed Rules

#### Rule 4 (Tier 2): Team Level Aggregation -- Added Aggregation Recovery Exception

```diff
- Studies reporting team as the unit of analysis MUST be excluded under Code 3.
+ NOTE (Individual-Measurement Aggregation Recovery):
+ If a study collected individual-level responses using "I" referent survey items
+ but subsequently aggregated them to team-level or dyad-level for analysis,
+ the underlying individual-level data may still exist.
+ Such papers should be coded as 1 = Include with a note indicating that
+ author contact is required to obtain the individual-level zero-order
+ correlation matrix.
+
+ This exception applies ONLY when:
+ (1) Survey items explicitly use individual referents ("I", "My")
+ (2) Individual-level responses were collected before aggregation
+ (3) Aggregation was a methodological choice, not measurement design
```

### Affected Papers (Example)

- `BSMA0385`, `BSMA0413`: Data collected with individual-level surveys then aggregated to team-level -> Switched from Exclude to Include

---

## V2 -> V3: Researcher Decision 2026-07-28 (Broad Rules)

**Git Commit:** `8086302`  
**Result Change:** Include 115 -> TBD (Significant additions expected)

### Changed Rules (3 Major Changes)

---

### 1. Rule 4: Aggregation Recovery -- Removed "Author Contact Required"

```diff
- NOTE (Individual-Measurement Aggregation Recovery):
-   coded as 1 = Include with a note indicating that
-   author contact is required
 
+ NOTE (Individual-Measurement Aggregation Recovery -- UNCONDITIONAL INCLUDE):
+   the paper MUST be coded as 1 = Include unconditionally.
+   [Researcher Decision 2026-07-28]
+   The previous "author contact required" qualifier has been removed.
```

> **Impact:** Conditional Includes from V2 become unconditional Includes. May add additional papers.

---

### 2. Rule 6: Communication Frequency -- Significantly Relaxed

```diff
- Variables that merely measure "communication frequency" (e.g., how often
-   someone emails or chats) without specifying a purposive boundary-spanning
-   action are INVALID and MUST be excluded under Code 1.
-
- NOTE (Test Case): Cross-departmental communication frequency
-   without specified purposive boundary-spanning action
-   -> INVALID (Code 1). This is mere communication, not purposive BSB.
 
+ [Researcher Decision 2026-07-28] Work-related communication frequency
+   across organizational or functional boundaries (e.g., "how often do you
+   discuss work-related issues with members of other departments")
+   IS a valid BSB operationalization and MUST BE INCLUDED.
+   Only purely non-work social communication frequency remains invalid.
```

> **Impact:** Many papers previously Excluded due to "simple communication frequency" are now Included. **This change has the largest impact.**

---

### 3. Rule 6: Network Measures -- Broad Inclusion

```diff
- VALID Network BSB (Do NOT Exclude):
-   (a) Advice-seeking network degree centrality
-   (b) E-I index
-   (c) Ego-network heterogeneity
- INVALID (Exclude):
-   (d) Burt's structural constraint measures
-   (c) Sociometric sensor data measuring mere proximity
 
+ VALID Network BSB (Do NOT Exclude):
+   ALL network-based measures of cross-boundary interaction ARE valid:
+   (a) Advice-seeking network degree centrality
+   (b) E-I index
+   (c) Ego-network heterogeneity
+   (d) Burt's structural constraint/structural holes     <-- NEW Include
+   (e) Sociometric sensor data (work-related)             <-- NEW Include
+   (f) ERGM parameters                                    <-- NEW Include
+   (g) Betweenness centrality and brokerage measures      <-- NEW Include
- INVALID (Exclude):
+   (a) Pure non-work social media interaction counts
+   (b) Adaptive Selling scales
```

> **Impact:** Previously Excluded targets such as Burt's structural holes, ERGM, and sociometric data are now fully Included.

---

### Quick Reference Table Changes

```diff
- | Individual-Measurement Aggregation Recovery | Rule 4 | INCLUDE (author contact required) |
+ | Individual-Measurement Aggregation Recovery | Rule 4 | INCLUDE (unconditional) |
+ | Work-related Communication Frequency         | Rule 6 | INCLUDE (if cross-boundary) |
+ | All Network Structural Metrics               | Rule 6 | INCLUDE (Burt, ERGM, etc.) |
```

---

## Comparing Rule Files Directly via Git

```bash
# V1 vs V2 (Strict -> AggRecovery)
git diff 0820472 da6da1a -- .agents/skills/include_exclude_pipeline/references/
 
# V2 vs V3 (AggRecovery -> Broad)
git diff da6da1a 8086302 -- .agents/skills/include_exclude_pipeline/references/
 
# V1 vs V3 (Strict -> Broad, Full Diff)
git diff 0820472 8086302 -- .agents/skills/include_exclude_pipeline/references/
```
