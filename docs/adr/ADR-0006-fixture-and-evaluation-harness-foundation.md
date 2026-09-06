# ADR-0006 — Fixture and Evaluation Harness Foundation

**Status:** ADOPTED

## Context

The project requires evaluation-driven development, but M0 must not
prematurely implement the full Evaluation domain.

## Decision

M0 provides:

- fixture directories for source, canonical, analysis, and evaluation data.
- `tests/support/fixture_loader.py`.
- UTF-8 source loading.
- expected JSON loading.
- explicit failure for missing fixture files.
- pytest as the evaluation-harness entry point.
- smoke-test foundation.
- architecture-test foundation.
- initial Contract-to-Test traceability.

The fixture loader MUST NOT perform:

- parsing.
- canonicalization.
- analysis.
- semantic processing.
- domain interpretation.

Fixtures must be synthetic, hand-authored, or appropriately anonymized.
Raw personal conversations MUST NOT enter Git.

## Rationale

This creates the minimum infrastructure required for reliable evaluation
without implementing later Evaluation Run/Trial/Decision semantics early.

## Alternatives Considered

- Full evaluation subsystem in M0 — rejected as premature.
- Domain-aware fixture loader — rejected.

## Consequences

Later evaluation capabilities can build on stable fixture and test
infrastructure without coupling M0 to business behavior.

## Related Contracts

- 09-EVALUATION-STRATEGY v0.3
- 10-IMPLEMENTATION-ROADMAP v0.4
- M0-IMPLEMENTATION-READINESS v0.7

## Supersedes

None.

## Superseded By

None.