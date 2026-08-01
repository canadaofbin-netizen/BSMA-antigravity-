# BSMA: Boundary Spanning Meta-Analysis

> Individual-level Boundary Spanning Behavior(BSB)의 선행변인과 결과변인에 대한 체계적 메타분석 프로젝트

---

## Project Overview

본 프로젝트는 조직 내/간 경계를 넘나드는 개인 수준의 Boundary Spanning Behavior(BSB)에 대한 포괄적 메타분석을 수행합니다. 701편의 학술 논문을 대상으로 AI-assisted screening pipeline과 수동 코딩을 병행하여 Include/Exclude 판정 및 효과크기 추출을 진행합니다.

---

## Directory Structure

```
BSMA ANTIGRAVITY/
├── 01_Academic_Papers/              701편 PDF (엄격한 네이밍: [ID] Author (Year) - Title.pdf)
├── 02_Reference_Manuals/            코딩 매뉴얼 및 참고 문서
├── 03_Validation_Results/           AI 검증 결과 엑셀
│   ├── BSMA_AI_Run_V1_AggRecovery.xlsx   V1: 115 Include / 586 Exclude
│   └── BSMA_AI_Run_V2_Broad.xlsx         V2: Broad rules (TBD)
├── 04_Reports/                      분석 리포트 (Match Rate, Screening Report)
├── 99_Archives_and_Backups/         백업 및 레거시 파일
│   ├── NEVER_CHANGE_IN_ANY_CASES/   불변 마스터 백업 (절대 수정 금지)
│   ├── Database_Milestones/         DB 스냅샷
│   ├── Prompt_Freezes/              파이프라인 규칙 스냅샷
│   ├── LLM_Audit_Trails/            AI 감사 로그
│   ├── Cleanup_Logs/                정리 작업 로그
│   └── Legacy/                      레거시 코드 및 규칙
├── .agents/                         AI 에이전트 설정 및 스킬
│   ├── AGENTS.md                    글로벌 규칙 (SSOT)
│   └── skills/                      모듈별 스킬 정의
├── scratch/                         임시 작업 파일 (.gitignore)
│   ├── extracted_texts/             PDF 추출 텍스트 (재사용)
│   ├── ocr_images/                  OCR 페이지 이미지
│   └── _disposable/                 일회성 스크립트/중간결과
├── BSMA_Master_Coding_Sheet.xlsx    마스터 코딩 시트 (50열, V1 기준)
├── CHANGELOG.md                     규칙 변경 이력
└── memory.md                        AI 작업 메모리
```

---

## Validation Versions

| Version | 파일명 | Include | Exclude | 규칙 특성 |
|---|---|---|---|---|
| **V1** (=V8) | `BSMA_AI_Run_V1_AggRecovery.xlsx` | 115 | 586 | Strict + Aggregation Recovery |
| **V2** (=V9) | `BSMA_AI_Run_V2_Broad.xlsx` | TBD | TBD | Broad (Researcher Decision 2026-07-28) |

규칙 변경 상세 내역은 [CHANGELOG.md](CHANGELOG.md)를 참조하세요.

---

## Branch Strategy

| Branch | 규칙 | 용도 |
|---|---|---|
| `main` | V1 AggRecovery | 기준 브랜치 |
| `strict-include-exclude-rules` | V1 AggRecovery | main 스냅샷 (잠금) |
| `develop` | V2 Broad | 작업용 |
| `loose-include-exclude-rules` | V2 Broad | V2 스냅샷 (잠금) |
| `feature/strict-pipeline` | V2 Broad | 기능 개발 |
| `experiment/v9-comparison` | V2 Broad | 실험용 |

**main과 나머지 브랜치의 차이는 Include/Exclude 규칙 파일 2개뿐입니다:**
- `screening_rules_core.md`
- `screening_edge_cases.md`

### Frozen Tags
- `v7-strict-rules-frozen`: V7 Strict 규칙 불변 스냅샷
- `v9-loose-rules-frozen`: V9 Broad 규칙 불변 스냅샷

---

## AI Pipeline

### Include/Exclude Screening
AI 기반 자동 스크리닝 파이프라인으로 701편의 논문을 병렬 처리합니다.

**사용법:**
- `/includeexclude` - 자동 스크리닝 파이프라인 실행
- `/workspace_lint` - 워크스페이스 위생 점검
- `/ask [질문]` - 읽기 전용 Q&A (파일 수정 없음)

### Core Rules
1. **Zero Guesswork Policy**: 숫자 결측 = `999`, 텍스트 결측 = `"Not Reported"`
2. **Verbatim Quote**: 모든 판정에 원문 인용 필수 (Col 16)
3. **Immutable Vault**: `NEVER_CHANGE_IN_ANY_CASES/` 절대 수정 금지
4. **SSOT**: `AGENTS.md`가 유일한 규칙 원천

---

## Key Files

| 파일 | 용도 |
|---|---|
| `BSMA_Master_Coding_Sheet.xlsx` | 마스터 코딩 시트 (50열, V1 기준) |
| `.agents/AGENTS.md` | AI 에이전트 글로벌 규칙 |
| `CHANGELOG.md` | V1/V2 규칙 변경 이력 |
| `memory.md` | AI 작업 메모리 및 판례 기록 |

---

## Quick Start

```bash
# 현재 브랜치 확인
git branch --list

# V1 vs V2 규칙 차이 확인
git diff main develop -- .agents/skills/include_exclude_pipeline/references/

# 스크리닝 파이프라인 실행 (Antigravity IDE에서)
/includeexclude

# 워크스페이스 점검
/workspace_lint
```
