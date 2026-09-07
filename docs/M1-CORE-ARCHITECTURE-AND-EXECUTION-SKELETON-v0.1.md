M1-CORE-ARCHITECTURE-AND-EXECUTION-SKELETON

Version: 0.1

Document Status: ADOPTED

Milestone Status: CLOSED

Final Engineering Review: PASS

Implementation Status: COMPLETE

======================================================================

1. DOCUMENT IDENTITY

======================================================================

Title: M1 - CORE ARCHITECTURE & EXECUTION SKELETON

Document Type: Adopted Architecture Specification

Version: 0.1

Date: 2026-09-07

Project: Arabic Conversation Analysis Engine

Status: ADOPTED

Milestone Status: CLOSED

======================================================================

2. LIFECYCLE AND AUTHORITY

======================================================================

Authority Order:

Project Charter

-> Adopted Specialized Specifications

-> ADRs

-> Implementation

Adopted ADRs:

- ADR-0001 through ADR-0008: ADOPTED

- ADR-0009: SUPERSEDED

- ADR-0010: ADOPTED

Foundation Documents 00-10 are authoritative even if not stored in the current Git repository.

M0 Status: ADOPTED, CLOSED

M1 Status: ADOPTED, CLOSED

M1 does not supersede M0.

======================================================================

3. INPUTS RECEIVED FROM M0

======================================================================

M0 provided:

- Initial source identity concepts (deferred in M1)

- Test fixture infrastructure (used only in `tests/`, not in production)

- Bootstrap entry point: `src/conversation_analysis/__main__.py`

- Existing architecture-test infrastructure (reused and extended)

No M0 implementation artifacts were adopted as production contracts.

======================================================================

4. PURPOSE

======================================================================

Establish the minimal, stable architectural substrate for M2-M6.

M1 defines only:

- Contract boundaries

- Dependency direction

- Port abstractions

- Registry abstraction

- Orchestration skeleton

M1 does NOT implement business logic, runtime behavior, or concrete adapters.

======================================================================

5. EXPLICIT NON-GOALS

======================================================================

M1 does NOT:

- Define exact Source Reference schema (for example, `source_id`, `revision_id`, coordinates)

- Implement a universal `generate()` method

- Define runtime generator execution semantics

- Freeze provenance persistence schema

- Define final severity taxonomy or threshold logic

- Implement one catch-all Result container

- Introduce CLI, API, UI, or new inbound adapters

- Implement Semantic Processing Port or External Processing Port

- Introduce new runtime dependencies

- Implement M6 Generator Registry runtime behavior

- Introduce Parser concrete types into Canonical architecture

- Introduce Provider SDK leakage

- Depend on `tests/support/fixture_loader.py` in production code

======================================================================

6. GOVERNING ARCHITECTURE INVARIANTS

======================================================================

- Core Dependency Graph MUST be ACYCLIC

- Infrastructure coupling inside Core MUST be prevented

- Provider SDK leakage MUST be prevented

- Parser concrete types inside Canonical MUST be prevented

- Delivery coupling MUST be prevented

- Core MUST NOT depend on Infrastructure

- Application MUST NOT depend on concrete Infrastructure implementations

- Core MUST NOT depend on Delivery

- Core MUST NOT depend on Provider SDK types

- Canonical architecture MUST NOT depend on concrete Parser implementations

- Infrastructure -> Application -> Core dependency direction MUST be preserved

Runtime Artifact Dependency != Compile-Time Module Dependency

Module != Processing Node

Source Processing Execution != Analysis Run

======================================================================

7. EXACT M1 SCOPE

======================================================================

M1 delivers:

1. Source Identity / Reference Contracts

2. Generator / Generator Version Contracts

3. Provenance / Lineage Contract

4. Coverage / Diagnostics Foundations

5. Domain Result / Operational Failure Contracts

6. Contract & Capability Registry Abstraction

7. Application Orchestration Substrate

8. Required Ports (5 total)

M1 does NOT deliver:

- Source Processing Execution

- Analysis Run

- DAG

- Generator Registry runtime behavior

- Artifact Envelope

- Parser implementations

- Concrete adapters

======================================================================

8. CORE CONTRACT BOUNDARIES

======================================================================

File:

`src/conversation_analysis/core/contracts.py`

Defines only neutral, extensible contract boundaries:

### Source Identity / Reference

- Abstract reference to a source artifact

- Exact identifier format and schema deferred

- No fields are required

- `source_id`, `revision_id`, coordinates, or similar identifiers are NOT normative in M1

### Generator / Generator Version

- Logical component identity associated with production of a Derived Artifact

- May later represent deterministic, rule-based, statistical, semantic, or LLM-based processing

- Generator version identity is part of the contract boundary

- No `generate()` method is defined in M1

- No concrete versioning scheme is enforced

### Provenance / Lineage

- Extensible lineage foundation

- May later reference Source, Source Reference, input artifacts, Generator, Configuration, Analysis Run, or other applicable lineage context

- Source-origin provenance may exist without a Generator

- Not reduced to a fixed tuple such as `source_id + generator_id + timestamp`

- Persistence schema is deferred

### Coverage / Diagnostics

- Neutral foundation for scope coverage and diagnostic signaling

- Concrete coverage representation is deferred

- No severity taxonomy is defined

- No thresholds are defined

- No aggregation rules are defined

### Domain Result

- Root for domain-level outcomes

- Separate from Operational / Processing Failure

- Does not imply a universal success/failure container

### Operational / Processing Failure

- Neutral root for non-domain operational or processing failures

- Concrete categories such as parsing, validation, policy, or provider failures are deferred

- Does not define runtime execution states

======================================================================

9. CONTRACT & CAPABILITY REGISTRY CONTRACT

======================================================================

File:

`src/conversation_analysis/application/registry.py`

Registry is an abstraction for:

- Version-safe contract and capability discovery

- Version-safe contract and capability resolution

It may later support resolution of:

- Source Representation Contract

- Source Format Contract

- Supported Variant Scope

- Parser capability

- Detection capability

- Required explicit inputs

- Compatibility metadata

- Conformance metadata

Registry does NOT:

- Perform Format Resolution itself

- Become the reproducibility source

- Implement M6 Generator Registry runtime behavior

- Define a generic mutable `register()/get()/list()` bag

Applicable contract and capability versions must later be pinnable in a resolution snapshot.

======================================================================

10. REQUIRED PORTS

======================================================================

File:

`src/conversation_analysis/application/ports.py`

M1 requires exactly five ports:

### 1. Source Access / Preservation Port

Substrate for M2.

May later support:

- Open immutable source revision

- Read source metadata

- Stream source content or bytes

- Bounded reads

- Range reads when supported

- Integrity verification when required

- Resolve source references or coordinates

Exact methods and types are deferred.

### 2. Canonical Persistence Port

Substrate for M4.

M1 does not define:

- Canonical implementation

- Canonical persistence schema

### 3. Derived Artifact Persistence Port

Substrate for M6.

M1 does not define:

- Artifact Envelope implementation

- Concrete artifact storage mechanism

### 4. Execution Metadata Port

Substrate for M6.

M1 does not define:

- Analysis Run schema

- Execution Attempt schema

- Runtime execution state machine

### 5. Telemetry Port

Substrate for diagnostics and operations across later milestones.

M1 does not define:

- Telemetry backend

- Concrete event schema

Ports do NOT include:

- Semantic Processing Port

- External Processing Port

======================================================================

11. APPLICATION ORCHESTRATION BOUNDARY

======================================================================

File:

`src/conversation_analysis/application/orchestration.py`

M1 orchestration is only the architectural coordination boundary.

It does NOT implement:

- Source Processing Execution

- Analysis Run

- Resolved Analysis Plan

- DAG

- Logical Node Execution

- Execution Attempt

- Runtime status machine

- Scheduling

- Retries

- Artifact Envelope

- Publication boundary

It provides the substrate for later milestones to compose Ports and capabilities without breaking dependency direction.

======================================================================

12. LAYER RESPONSIBILITIES

======================================================================

Core:

- Domain contracts only

- No Application dependency

- No Infrastructure dependency

- No Delivery dependency

- No Provider SDK dependency

Application:

- Orchestration

- Ports

- Registry abstraction

- May depend on Core

- Must not depend on concrete Infrastructure implementations

Infrastructure:

- No concrete M1 implementation required

- Reserved for later milestone adapters and implementations

Delivery:

- No new M1 implementation required

- M0 bootstrap remains:

`src/conversation_analysis/__main__.py`

Compile-time dependency direction:

Infrastructure -> Application -> Core

Core dependency graph MUST remain acyclic.

======================================================================

13. APPROVED FILE / MODULE PLAN

======================================================================

```text
src/conversation_analysis/
|-- core/
|   |-- __init__.py        REUSE
|   \-- contracts.py       NEW
|
|-- application/
|   |-- __init__.py        REUSE
|   |-- registry.py        NEW
|   |-- ports.py           NEW
|   \-- orchestration.py   NEW
|
|-- delivery/
|   \-- __init__.py        REUSE
|
|-- infrastructure/
|   \-- __init__.py        REUSE
|
|-- __init__.py            REUSE
\-- __main__.py            REUSE
```

No additional production modules were introduced unless strictly required by the M1 contract.

======================================================================

14. EXISTING ARTIFACTS REUSED

======================================================================

- `src/conversation_analysis/__main__.py` - M0 bootstrap

- `tests/` - M0 fixture infrastructure, used only in tests

- `tests/support/fixture_loader.py` - remains test-only and is not imported by production code

- Existing Python/AST-based architecture-test infrastructure

- Python standard library

- pytest

- Ruff

- mypy

No new runtime dependencies were introduced.

======================================================================

15. ARCHITECTURE AND CONFORMANCE TESTS

======================================================================

Implemented tests verify:

1. Core contracts importability

2. Source Identity / Reference contract boundary

3. Generator / Generator Version contract boundary

4. Provenance extensibility and non-overbinding

5. Coverage / Diagnostics foundation neutrality

6. Domain Result vs Operational Failure separation

7. Contract & Capability Registry resolution abstraction

8. Required Ports exist and contain no Infrastructure types

9. Application orchestration imports only permitted dependencies

10. Core dependency graph is acyclic

11. Dependency direction conforms

12. Core contains no Infrastructure imports

13. Core / Application contain no Provider SDK imports

14. Core contains no Parser concrete types

15. Core contains no Delivery imports

16. `src/` contains no dependency on `tests/support/fixture_loader.py`

Implementation state:

`IMPLEMENTED / PASS`

Final pytest result:

`50 passed`

======================================================================

16. EVALUATION EVIDENCE

======================================================================

Final M1 evidence:

- pytest: 50 passed

- Ruff format: PASS

- Ruff check: PASS

- mypy strict: PASS

- git diff --check: PASS

- Core acyclicity: PASS

- Dependency direction: PASS

- Architecture boundary conformance: PASS

- Contract-to-Test traceability: PASS

Implementation commit:

`8811175c839af11490983b9cff1c18af15216c60`

Commit message:

`feat: complete M1 core architecture and execution skeleton`

======================================================================

17. CONTRACT-TO-TEST TRACEABILITY

======================================================================

Each M1 contract and architectural boundary has executable test coverage.

Primary mappings:

- `src/conversation_analysis/core/contracts.py`
  -> `tests/architecture/test_m1_contracts.py`

- `src/conversation_analysis/application/registry.py`
  -> `tests/architecture/test_m1_registry.py`

- `src/conversation_analysis/application/ports.py`
  -> `tests/architecture/test_m1_ports.py`

- `src/conversation_analysis/application/orchestration.py`
  -> `tests/architecture/test_m1_orchestration.py`

- Dependency direction, Core acyclicity, Provider SDK leakage, Parser leakage, Delivery coupling, Infrastructure coupling, and production fixture-loader isolation
  -> `tests/architecture/test_m1_dependencies.py`

Authoritative traceability matrix:

`docs/contract-test-traceability.md`

Traceability Status:

PASS

Tests verify contracts; they do not redefine them.

======================================================================

18. REQUIRED DELIVERY PACKAGE

======================================================================

Production files delivered:

- `src/conversation_analysis/core/contracts.py`

- `src/conversation_analysis/application/registry.py`

- `src/conversation_analysis/application/ports.py`

- `src/conversation_analysis/application/orchestration.py`

Architecture and conformance tests delivered:

- `tests/architecture/test_m1_contracts.py`

- `tests/architecture/test_m1_registry.py`

- `tests/architecture/test_m1_ports.py`

- `tests/architecture/test_m1_orchestration.py`

- `tests/architecture/test_m1_dependencies.py`

Supporting evidence:

- `docs/contract-test-traceability.md`

Other delivery conditions:

- Existing `__init__.py` files reused

- No CLI introduced

- No API introduced

- No UI introduced

- No new Delivery adapter introduced

- No new runtime dependency introduced

- No Provider SDK coupling introduced

- No concrete Parser coupling introduced

======================================================================

19. CLOSURE GATE

======================================================================

M1 closure requirements have been satisfied:

- All adopted M1 deliverables implemented: PASS

- Core contracts conform: PASS

- Contract & Capability Registry abstraction conforms: PASS

- Required Ports conform: PASS

- Application orchestration skeleton conforms: PASS

- Core dependency graph is acyclic: PASS

- Infrastructure -> Application -> Core dependency direction conforms: PASS

- No Infrastructure coupling inside Core: PASS

- No Delivery coupling inside Core: PASS

- No Provider SDK leakage: PASS

- No Parser concrete types leak into Canonical architecture: PASS

- No production dependency on test fixture infrastructure: PASS

- Ruff format: PASS

- Ruff check: PASS

- mypy strict: PASS

- pytest: PASS - 50 passed

- Contract-to-Test traceability updated: PASS

- No known regression against M0 baseline: PASS

Open Blockers:

0

M1 Closure Decision:

CLOSED

======================================================================

20. DOWNSTREAM HANDOFF

======================================================================

M1 provides the architecture substrate to M2-M6 and later semantic processing work.

### M2

Ownership:

- Source Intake

- Preservation

- Source Processing Execution

M1 substrate provided:

- Source Identity / Reference foundation

- Source Access / Preservation Port

- Application coordination boundary

### M3

Ownership:

- First Supported Source Format

- First concrete parser

M1 substrate provided:

- Source Identity / Reference Contract

- Contract & Capability Registry abstraction

- Applicable application Ports

### M4

Ownership:

- Conversation Unit Resolution

- Canonicalization implementation

M1 substrate provided:

- Canonical Persistence Port

- Core contract boundaries

### M5

Ownership:

- P0 Integration

- Evaluation Gate

M1 substrate provided:

- Coverage / Diagnostics foundation

- Domain Result / Operational Failure separation

### M6

Ownership:

- Analysis Run

- Resolved Analysis Plan

- DAG

- Logical Node Execution

- Execution Attempt

- Generator Registry runtime behavior

- Artifact Envelope

- Publication boundary

- Lineage runtime

- Basic re-run

M1 substrate provided:

- Generator / Generator Version foundation

- Derived Artifact Persistence Port

- Execution Metadata Port

- Telemetry Port

- Contract & Capability Registry abstraction

- Orchestration substrate

### M11

Ownership:

- Semantic Processing Foundation

- Runtime semantic/provider integration

M1 substrate provided:

- Provider-independent Core contracts

- Registry abstraction

- Applicable Ports and architecture boundaries

M1 does NOT freeze concrete method names or runtime semantics for downstream milestones.

======================================================================

21. DEFERRED DECISIONS

======================================================================

The following decisions remain intentionally deferred to their owning downstream specifications or milestones:

- Exact Source Reference schema

- Exact Source identifier format

- Exact Source Revision identifier format

- Provenance persistence schema

- Coverage concrete representation

- Diagnostics severity taxonomy

- Diagnostics thresholds

- Diagnostics aggregation rules

- Operational Failure concrete categories

- Generator Version scheme

- Registry concrete resolution mechanism

- Registry version pinning mechanism

- Port concrete method signatures

- Port concrete data types

- Orchestration coordination logic

- Telemetry event schema

- Semantic Processing Port introduction timing

- External Processing Port introduction timing

These deferred decisions are not M1 blockers.

======================================================================

22. RISKS AND AMBIGUITIES

======================================================================

No open material architecture ambiguity blocks M1 closure.

All unresolved implementation details are explicitly deferred to their owning downstream milestones.

M1 remains intentionally minimal and non-overbinding.

======================================================================

23. UPSTREAM REVISION ASSESSMENT

======================================================================

Upstream Revision Required:

NO

Adopted ADRs 0001-0008 and 0010 remain consistent with M1.

ADR-0009 remains SUPERSEDED and excluded.

No upstream revision is required for M1 closure.

======================================================================

24. PROJECT OWNER DECISION ASSESSMENT

======================================================================

Repository visibility is not an open M1 adoption decision.

ADR-0010 remains authoritative.

Open Material Architecture Decisions:

0

Open Blockers:

0

Project Owner adopted M1 v0.1 on 2026-09-07.

M1 implementation and quality gates completed on 2026-09-07.

======================================================================

25. CLOSURE DECISION BLOCK

======================================================================

Document Status:

ADOPTED

Milestone Status:

CLOSED

Implementation Status:

COMPLETE

Implementation Authorization:

COMPLETED

Final Engineering Review:

PASS

Upstream Revision Required:

NO

Open Material Architecture Decisions:

0

Open Blockers:

0

Next Lifecycle Step:

M2 - SOURCE INTAKE, PRESERVATION & SOURCE PROCESSING EXECUTION

======================================================================

26. M1 CLOSURE EVIDENCE

======================================================================

Implementation Status:

COMPLETE

Milestone Status:

CLOSED

Open Blockers:

0

Verified Quality Gate:

- Ruff format: PASS

- Ruff check: PASS

- mypy strict: PASS

- pytest: 50 passed

- git diff --check: PASS

- Contract-to-Test traceability: PASS

Implementation Commit:

`8811175c839af11490983b9cff1c18af15216c60`

Implementation Commit Message:

`feat: complete M1 core architecture and execution skeleton`

Next Lifecycle Step:

M2 - SOURCE INTAKE, PRESERVATION & SOURCE PROCESSING EXECUTION

======================================================================

M1_CLOSED