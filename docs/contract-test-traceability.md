# Contract-to-Test Traceability

## Purpose

This document provides the initial M0 mapping between adopted
implementation-readiness requirements and executable tests or explicit
verification evidence.

The adopted specification remains authoritative. Tests verify contracts;
they do not redefine them.

| Contract / Requirement | Evidence / Test | State |
|---|---|---|
| CPython >=3.13,<3.14 | Project Runtime = CPython 3.13.15 | PASS |
| Repository-external isolated environment | `sys.prefix != sys.base_prefix` | PASS |
| No shared site-packages inheritance | `include-system-site-packages = false` | PASS |
| Project pip operational | Environment-local pip 26.2.1 | PASS |
| Build backend available | setuptools 84.0.0 in Project Environment | PASS |
| pytest available | pytest 9.1.1 | PASS |
| Ruff available | Ruff 0.16.5 | PASS |
| mypy available | mypy 2.3.1 | PASS |
| Editable installation | `arabic-conversation-analysis 0.0.0` editable install | PASS |
| Import package operational | `conversation_analysis` import | PASS |
| Runtime entry point operational | `tests/conformance/test_m0_smoke.py::test_runtime_entrypoint_returns_success` | PASS |
| UTF-8 fixture loading | `tests/unit/test_fixture_loader.py::test_reads_utf8_source` | PASS |
| Expected JSON loading | `tests/unit/test_fixture_loader.py::test_reads_expected_json` | PASS |
| Missing fixture case fails explicitly | `test_missing_case_fails_explicitly` | PASS |
| Missing source fails explicitly | `test_missing_source_fails_explicitly` | PASS |
| Missing expected JSON fails explicitly | `test_missing_expected_json_fails_explicitly` | PASS |
| Allowed architecture dependency graph | `tests/architecture/test_dependency_rules.py` | PASS |
| Forbidden architecture dependency detection | `tests/architecture/test_dependency_rules.py` | PASS |
| Ruff formatting | Local Quality Gate | PASS |
| Ruff linting | Local Quality Gate | PASS |
| mypy strict production source | Local Quality Gate | PASS |
| Full pytest suite | Local Quality Gate — 11 passed | PASS |
| GitHub remote with owner-selected visibility | Current repository PUBLIC | PASS |
| `origin` configured | Git/GitHub evidence | PASS |
| Initial push | Git/GitHub evidence | PASS |

## Traceability Rule

Material adopted `MUST` and `MUST NOT` requirements should progressively
map to executable Conformance Tests or explicit verification evidence.

A passing test cannot weaken or replace its governing contract.