# BSMA Validation Rule Changelog

> 각 Validation 버전 간 규칙 변경사항과 그로 인한 결과 차이를 기록합니다.

---

## Version Summary

| Version | 파일명 | Include | Exclude | 규칙 특성 |
|---|---|---|---|---|
| **V1** (=V7) | `BSMA_AI_Run_V1_Strict.xlsx` | 106 | 595 | Original Strict |
| **V2** (=V8) | `BSMA_AI_Run_V2_AggRecovery.xlsx` | 115 | 586 | Strict + Aggregation Recovery |
| **V3** (=V9) | `BSMA_AI_Run_V3_Broad.xlsx` | TBD | TBD | Broad (Researcher Decision) |

---

## V1 -> V2: Aggregation Recovery Rule 추가

**Git Commits:** `0820472` -> `da6da1a`  
**결과 변화:** Include 106 -> 115 (+9편)

### 변경된 규칙

#### Rule 4 (Tier 2): Team Level Aggregation -- Aggregation Recovery Exception 추가

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

### 영향받은 논문 (예시)

- `BSMA0385`, `BSMA0413`: 개인 수준 설문으로 수집 후 팀 수준으로 집계 -> Exclude에서 Include로 전환

---

## V2 -> V3: Researcher Decision 2026-07-28 (Broad Rules)

**Git Commit:** `8086302`  
**결과 변화:** Include 115 -> TBD (상당수 추가 예상)

### 변경된 규칙 (3가지 주요 변경)

---

### 1. Rule 4: Aggregation Recovery -- "Author Contact Required" 제거

```diff
- NOTE (Individual-Measurement Aggregation Recovery):
-   coded as 1 = Include with a note indicating that
-   author contact is required

+ NOTE (Individual-Measurement Aggregation Recovery -- UNCONDITIONAL INCLUDE):
+   the paper MUST be coded as 1 = Include unconditionally.
+   [Researcher Decision 2026-07-28]
+   The previous "author contact required" qualifier has been removed.
```

> **영향:** V2에서 이미 Include된 논문들의 조건부 Include가 무조건 Include로 강화. 추가 논문 포함 가능.

---

### 2. Rule 6: Communication Frequency -- 대폭 완화

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

> **영향:** 기존에 "단순 커뮤니케이션 빈도"로 Exclude되었던 다수 논문이 Include로 전환. **가장 큰 영향을 미친 변경.**

---

### 3. Rule 6: Network Measures -- 전면 포함

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

> **영향:** Burt's structural holes, ERGM, sociometric 데이터 등 기존 Exclude 대상이 전면 Include로 전환.

---

### Quick Reference Table 변경

```diff
- | Individual-Measurement Aggregation Recovery | Rule 4 | INCLUDE (author contact required) |
+ | Individual-Measurement Aggregation Recovery | Rule 4 | INCLUDE (unconditional) |
+ | Work-related Communication Frequency         | Rule 6 | INCLUDE (if cross-boundary) |
+ | All Network Structural Metrics               | Rule 6 | INCLUDE (Burt, ERGM, etc.) |
```

---

## Git에서 규칙 파일 직접 비교하기

```bash
# V1 vs V2 (Strict -> AggRecovery)
git diff 0820472 da6da1a -- .agents/skills/include_exclude_pipeline/references/

# V2 vs V3 (AggRecovery -> Broad)
git diff da6da1a 8086302 -- .agents/skills/include_exclude_pipeline/references/

# V1 vs V3 (Strict -> Broad, 전체 차이)
git diff 0820472 8086302 -- .agents/skills/include_exclude_pipeline/references/
```
