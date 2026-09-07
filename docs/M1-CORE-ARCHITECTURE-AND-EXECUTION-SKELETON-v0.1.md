M1-CORE-ARCHITECTURE-AND-EXECUTION-SKELETON  
Version: 0.1  
Document Status: ADOPTED  
Milestone Status: OPEN  
Final Engineering Review: PASS  
Implementation Authorization: AUTHORIZED  
Next Lifecycle Step: M1 IMPLEMENTATION  

---

### 1. Document Identity

- **Document Title**: M1 ظ¤ Core Architecture & Execution Skeleton  
- **Version**: 0.1  
- **Document Status**: ADOPTED  
- **Milestone Status**: OPEN  
- **Final Engineering Review**: PASS  
- **Adoption Date**: 2026-09-07  
- **Project**: Arabic Conversation Analysis Engine  
- **Governing Authority**: Project Charter ظْ Adopted Specialized Specifications ظْ ADRs (0001ظô0008, 0010) ظْ M1  

---

### 2. Lifecycle and Authority

- M1 supersedes M0 as the active milestone for architectural foundation work.  
- M0 remains authoritative for historical context and baseline regression checks.  
- M1 does *not* supersede M0ظآs closure; M0 is closed.  
- ADR-0009 is superseded and excluded from M1 scope.  
- All adopted ADRs (0001ظô0008, 0010) are binding.  
- Repository visibility (PUBLIC/PRIVATE) is governed by ADR-0010 and is *not* an M1 design decision.  

---

### 3. Inputs Received from M0

- M0 ظ¤ Implementation Readiness v0.8 (ADOPTED, CLOSED)  
- M0 smoke fixture infrastructure remains *test-only*; no production contracts derived from it.  
- M0 baseline tests may be referenced as historical PASS evidence where observed.  
- M0 fixture loader (`tests/support/fixture_loader.py`) must *not* be imported by production code.  

---

### 4. Purpose

To establish the minimal, architecture-compliant substrate for the Arabic Conversation Analysis Engine, enabling M2ظôM6 execution while enforcing strict dependency direction, modularity, and extensibility.  
M1 delivers only the *contractual and structural skeleton* ظ¤ no business logic, runtime semantics, or concrete implementations beyond what is strictly required for architectural boundaries.

---

### 5. Explicit Non-Goals

M1 does *not*:

- Define concrete identifier formats (e.g., `source_id`, `revision_id`, `coordinates`) ظ¤ exact schema deferred.  
- Implement `generate()` methods or generator execution semantics.  
- Define persistence schemas (Provenance, Canonical, Artifact Envelope, Execution Metadata).  
- Introduce CLI, API, UI, or new delivery adapters.  
- Implement Source Processing Execution, Analysis Run, DAG, or Logical Node Execution.  
- Introduce Provider SDK types, Parser concrete types, or Delivery coupling in Core.  
- Define final severity taxonomy, thresholds, aggregation rules, or retry semantics.  
- Implement M6 Generator Registry runtime behavior.  
- Introduce Semantic Processing Port or External Processing Port.  
- Add new runtime dependencies beyond Python stdlib, pytest, Ruff, mypy, and existing architecture-test infrastructure.

---

### 6. Governing Architecture Invariants

- **Core Dependency Graph MUST be ACYCLIC**.  
- **Core MUST NOT depend on Infrastructure**.  
- **Application MUST NOT depend on concrete Infrastructure implementations**.  
- **Core MUST NOT depend on Delivery**.  
- **Core MUST NOT depend on Provider SDK types**.  
- **Canonical architecture MUST NOT depend on concrete Parser implementations**.  
- **Infrastructure ظْ Application ظْ Core** dependency direction enforced at compile time.  
- **Module ظëب Processing Node**; **Runtime Artifact Dependency ظëب Compile-Time Module Dependency**.  
- **Source Processing Execution ظëب Analysis Run**.

---

### 7. Exact M1 Scope

M1 delivers only:

1. **Source Identity / Reference Contracts**  
2. **Generator / Generator Version Contracts**  
3. **Provenance / Lineage Contract Boundary**  
4. **Coverage / Diagnostics Foundations**  
5. **Domain Result vs Operational / Processing Failure Contracts**  
6. **Contract & Capability Registry Abstraction**  
7. **Application Orchestration Substrate**  
8. **Required Ports (5)**  
9. **Approved Minimal File Plan**  
10. **Architecture & Conformance Test Plan**

No runtime behavior, no concrete adapters, no business logic.

---

### 8. Core Contract Boundaries

`src/conversation_analysis/core/contracts.py` defines *only* the following neutral contract roots:

- **Source Identity / Reference**  
  - Abstract reference to a source artifact.  
  - *Not* raw_content, in-memory object, or frozen schema.  
  - Exact identifier format and schema deferred.

- **Generator Identity / Version**  
  - Logical component producing a Derived Artifact.  
  - May later be deterministic, rule-based, statistical, semantic, or LLM-based.  
  - No `generate()` method defined.

- **Provenance / Lineage**  
  - Extensible origin explanation (may reference Source, Generator, Configuration, etc.).  
  - Source-origin provenance may exist without Generator.  
  - No fixed tuple (e.g., `source_id + generator_id + timestamp`).  
  - Persistence schema deferred.

- **Coverage / Diagnostics**  
  - Neutral foundation for scope coverage and diagnostic signaling.  
  - No severity taxonomy, thresholds, or aggregation rules.  
  - Concrete representation deferred.

- **Domain Result**  
  - Root for domain-level outcomes (e.g., parsed, canonicalized, validated).  
  - Separate from operational failures.

- **Operational / Processing Failure**  
  - Neutral root for non-domain failures (e.g., parsing, validation, provider, policy).  
  - Concrete categories deferred.

All contracts are *extensible*, *non-overbinding*, and *future-proofed*.

---

### 9. Contract & Capability Registry Contract

`src/conversation_analysis/application/registry.py` defines:

- **Registry Abstraction**  
  - Responsible for *version-safe* contract/capability discovery and resolution.  
  - Capable of resolving:  
    - Source Representation Contract  
    - Source Format Contract  
    - Supported Variant Scope  
    - Parser capability  
    - Detection capability  
    - Required explicit inputs  
    - Compatibility / Conformance metadata  
  - Registry *does not* perform Format Resolution.  
  - Registry *does not* become the reproducibility source.  
  - Applicable contract/capability versions must later be pinnable in a resolution snapshot.  
  - No `register()/get()/list()` interface defined in M1.

---

### 10. Required Ports

`src/conversation_analysis/application/ports.py` defines *only* the following 5 ports:

1. **Source Access / Preservation Port**  
   - Substrate for M2.  
   - May support: immutable source revision, metadata read, stream content, bounded/range reads, integrity verification, reference resolution.  
   - Exact methods/types deferred.

2. **Canonical Persistence Port**  
   - Substrate for M4.  
   - No Canonical implementation or storage schema in M1.

3. **Derived Artifact Persistence Port**  
   - Substrate for M6.  
   - No Artifact Envelope implementation in M1.

4. **Execution Metadata Port**  
   - Substrate for M6.  
   - No AnalysisRun / ExecutionAttempt schema in M1.

5. **Telemetry Port**  
   - Substrate for diagnostics/operations across M2ظôM6.  
   - No backend or event schema in M1.

*No Semantic Processing Port or External Processing Port defined in M1.*

---

### 11. Application Orchestration Boundary

`src/conversation_analysis/application/orchestration.py` defines:

- Minimal coordination substrate for Ports and capabilities.  
- *No* Source Processing Execution, Analysis Run, DAG, scheduling, retries, Artifact Envelope, or status machine.  
- Ensures later milestones compose without violating dependency direction.

---

### 12. Layer Responsibilities

| Layer | Responsibility | M1 Scope |
|-------|----------------|----------|
| **Core** | Domain contracts only | Contracts + Registry abstraction (as substrate) |
| **Application** | Orchestration + Ports + Registry | Ports, Registry, Orchestration |
| **Infrastructure** | Concrete implementations | *None* in M1 |
| **Delivery** | Inbound adapters (CLI/API/UI) | *None* in M1 |

Core must not import Application, Infrastructure, or Delivery.  
Application must not import Infrastructure implementations.

---

### 13. Approved File/Module Plan

```
src/conversation_analysis/
ظ¤é
ظ¤£ظ¤ظ¤ core/
ظ¤é   ظ¤£ظ¤ظ¤ __init__.py                 REUSE
ظ¤é   ظ¤¤ظ¤ظ¤ contracts.py                NEW
ظ¤é
ظ¤£ظ¤ظ¤ application/
ظ¤é   ظ¤£ظ¤ظ¤ __init__.py                 REUSE
ظ¤é   ظ¤£ظ¤ظ¤ registry.py                 NEW
ظ¤é   ظ¤£ظ¤ظ¤ ports.py                    NEW
ظ¤é   ظ¤¤ظ¤ظ¤ orchestration.py            NEW
ظ¤é
ظ¤£ظ¤ظ¤ delivery/
ظ¤é   ظ¤¤ظ¤ظ¤ __init__.py                 REUSE
ظ¤é
ظ¤£ظ¤ظ¤ infrastructure/
ظ¤é   ظ¤¤ظ¤ظ¤ __init__.py                 REUSE
ظ¤é
ظ¤£ظ¤ظ¤ __init__.py                     REUSE
ظ¤¤ظ¤ظ¤ __main__.py                     REUSE
```

No additional modules introduced unless strictly required by M1 contract.

---

### 14. Existing Artifacts to Reuse

- `src/conversation_analysis/__main__.py` ظ¤ M0 bootstrap remains sole entry point.  
- `tests/` ظ¤ M0 fixture infrastructure remains *test-only*.  
- `tests/support/fixture_loader.py` ظ¤ *not* imported by production code.  
- Existing architecture-test infrastructure (Python/AST-based) ظ¤ reused and extended.

---

### 15. Architecture and Conformance Test Plan

M1 tests must verify:

1. Core contracts importability.  
2. Source identity/reference contract boundary.  
3. Generator/version contract boundary.  
4. Provenance extensibility/non-overbinding.  
5. Coverage/Diagnostics foundation neutrality.  
6. Domain Result vs Operational Failure separation.  
7. Contract & Capability Registry resolution abstraction.  
8. Required Ports exist and contain no infrastructure types.  
9. Application orchestration imports only permitted dependencies.  
10. Core dependency graph is acyclic.  
11. Dependency direction conforms (Infrastructure ظْ Application ظْ Core).  
12. Core contains no Infrastructure imports.  
13. Core/Application contain no Provider SDK imports.  
14. Core contains no Parser concrete types.  
15. Core contains no Delivery imports.  
16. `src/` contains no dependency on `tests/support/fixture_loader.py`.

*All tests marked:* `PLANNED / NOT YET IMPLEMENTED` until executed.

---

### 16. Evaluation Evidence Plan

- Reuse and extend existing M0 architecture-test infrastructure.  
- No new tools introduced (e.g., pydeps).  
- Evidence must be observable via existing Python/AST-based architecture tests.  
- M0 evidence may be referenced as historical PASS only where observed.

---

### 17. Contract-to-Test Traceability Plan

- Each contract root in `core/contracts.py` must be traceable to at least one test.  
- Each port in `application/ports.py` must be traceable to at least one test.  
- Registry abstraction in `application/registry.py` must be traceable to at least one test.  
- Orchestration boundary in `application/orchestration.py` must be traceable to at least one test.  
- Traceability matrix updated post-implementation.

---

### 18. Required Delivery Package

- `src/conversation_analysis/core/contracts.py`  
- `src/conversation_analysis/application/registry.py`  
- `src/conversation_analysis/application/ports.py`  
- `src/conversation_analysis/application/orchestration.py`  
- All `__init__.py` files as per plan  
- No new runtime dependencies  
- No CLI/API/UI entry points  
- No `src/conversation_analysis/delivery/__main__.py`

---

### 19. Closure Gate

M1 closes only when:

- All adopted M1 deliverables implemented.  
- Core contracts conform.  
- Contract & Capability Registry abstraction conforms.  
- Required Ports conform.  
- Application orchestration skeleton conforms.  
- Core dependency graph is acyclic.  
- Dependency direction conforms.  
- No Infrastructure coupling in Core.  
- No Delivery coupling in Core.  
- No Provider SDK leakage.  
- No Parser concrete types in Canonical architecture.  
- No production dependency on `tests/support/fixture_loader.py`.  
- `ruff format` passes.  
- `ruff check` passes.  
- `mypy --strict` passes.  
- `pytest` passes.  
- Contract-to-Test traceability updated.  
- No known regression against M0 baseline.

---

### 20. Downstream Handoff

| Milestone | Ownership | M1 Substrate Provided |
|-----------|-----------|------------------------|
| **M2** | Source Intake, Preservation, Source Processing Execution | Source Access / Preservation Port |
| **M3** | First Supported Source Format, concrete parser | Source Identity Contract, Ports |
| **M4** | Conversation Unit Resolution, Canonicalization | Canonical Persistence Port |
| **M5** | P0 Integration, Evaluation Gate | Coverage/Diagnostics, Result/Error Contracts |
| **M6** | Analysis Run, DAG, Generator Registry, Artifact Envelope, lineage runtime, basic re-run | Derived Artifact Persistence Port, Execution Metadata Port, Registry Abstraction, Telemetry Port |
| **M11** | Semantic Processing Foundation, runtime provider integration | Contract & Capability Registry, Ports (as needed) |

No future milestone dependencies on concrete M1 method names.

---

### 21. Deferred Decisions

- Exact Source Reference schema and identifier format.  
- Provenance persistence schema.  
- Coverage representation.  
- Diagnostics severity taxonomy.  
- Operational Failure concrete categories.  
- Registry concrete resolution mechanism.  
- Port method signatures and types.  
- Registry version pinning mechanism.  
- Telemetry event schema.  
- Semantic Processing Port / External Processing Port introduction timing.

---

### 22. Risks and Ambiguities

- None identified.  
- All architectural boundaries are explicitly deferred where needed.  
- M1 is intentionally minimal and non-committal.

---

### 23. Upstream Revision Assessment

- **Upstream Revision Required**: NO  
- All ADRs (0001ظô0008, 0010) are consistent with M1 design.  
- No ADR conflicts.  
- ADR-0009 (superseded) excluded.

---

### 24. Project Owner Decision Assessment

- **Open Material Architecture Decisions**: 0  
- Repository visibility (ADR-0010) is not an M1 design decision.  
- Project Owner explicitly adopted M1 v0.1 on 2026-09-07.

---

### 25. Adoption Decision Block

Document Status:  
**ADOPTED**

Implementation Authorization:  
**AUTHORIZED**

Upstream Revision Required:  
**NO**

Open Material Architecture Decisions:  
**0**

Next Lifecycle Step:  
**M1 IMPLEMENTATION**

---

M1_ADOPTED_DOCUMENT_READY
