# Contract-to-Test Traceability

## Purpose

This document provides the mapping between adopted implementation-readiness
requirements and executable tests or explicit verification evidence for M0 and M1.

The adopted specification remains authoritative. Tests verify contracts;
they do not redefine them.

## M0 Traceability

| Contract / Requirement | Evidence / Test | State |
|---|---|---|
| CPython >=3.13,<3.14 | Project Runtime = CPython 3.13.15 | PASS |
| Repository-external isolated environment | `sys.prefix != sys.base_prefix` | PASS |
| No shared site-packages inheritance | `include-system-site-packages = false` | PASS |
| Project pip operational | pip 26.2.1 | PASS |
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

## M1 Traceability

| Contract / Requirement | Evidence / Test | State |
|---|---|---|
| Source Identity / Reference Contract | `tests/architecture/test_m1_contracts.py::test_source_identity_reference_contract_boundary` | PASS |
| Generator Identity / Version Contract | `tests/architecture/test_m1_contracts.py::test_generator_version_contract_boundary` | PASS |
| Provenance / Lineage Contract Boundary | `tests/architecture/test_m1_contracts.py::test_provenance_extensibility_non_overbinding` | PASS |
| Coverage / Diagnostics Foundations | `tests/architecture/test_m1_contracts.py::test_coverage_diagnostics_foundation_neutrality` | PASS |
| Domain Result vs Operational Failure Contracts | `tests/architecture/test_m1_contracts.py::test_domain_result_vs_operational_failure_separation` | PASS |
| Contract & Capability Registry Abstraction | `tests/architecture/test_m1_registry.py::test_registry_abstraction_exists` | PASS |
| Required Ports (5) Exist | `tests/architecture/test_m1_ports.py::test_required_ports_exist` | PASS |
| Source Access / Preservation Port | `tests/architecture/test_m1_ports.py::test_source_access_preservation_port` | PASS |
| Canonical Persistence Port | `tests/architecture/test_m1_ports.py::test_canonical_persistence_port` | PASS |
| Derived Artifact Persistence Port | `tests/architecture/test_m1_ports.py::test_derived_artifact_persistence_port` | PASS |
| Execution Metadata Port | `tests/architecture/test_m1_ports.py::test_execution_metadata_port` | PASS |
| Telemetry Port | `tests/architecture/test_m1_ports.py::test_telemetry_port` | PASS |
| Application Orchestration Substrate | `tests/architecture/test_m1_orchestration.py::test_orchestration_boundary_exists` | PASS |
| Core contracts importability | `tests/architecture/test_m1_contracts.py::test_core_contracts_importability` | PASS |
| Core contains no Infrastructure imports | `tests/architecture/test_m1_dependencies.py::test_no_infrastructure_coupling_in_core` | PASS |
| Core contains no Delivery imports | `tests/architecture/test_m1_dependencies.py::test_no_delivery_coupling_in_core` | PASS |
| Core/Application contain no Provider SDK imports | `tests/architecture/test_m1_dependencies.py::test_no_provider_sdk_leakage` | PASS |
| Core contains no Parser concrete types | `tests/architecture/test_m1_dependencies.py::test_no_parser_concrete_types_in_canonical_architecture` | PASS |
| Core dependency graph is acyclic | `tests/architecture/test_m1_dependencies.py::test_core_dependency_graph_is_acyclic` | PASS |
| Dependency direction conforms | `tests/architecture/test_m1_dependencies.py::test_dependency_direction_conforms` | PASS |
| No production dependency on fixture_loader | `tests/architecture/test_m1_dependencies.py::test_no_fixture_loader_dependency_in_src` | PASS |

## Traceability Rule

Material adopted `MUST` and `MUST NOT` requirements should progressively
map to executable Conformance Tests or explicit verification evidence.

A passing test cannot weaken or replace its governing contract.
