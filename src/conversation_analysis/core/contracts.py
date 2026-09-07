"""Core contracts for the Arabic Conversation Analysis Engine.

This module defines neutral contract roots that are extensible, non-overbinding,
and future-proofed. These contracts form the foundation for all domain concepts
without specifying concrete implementations or behaviors.
"""

from abc import ABC


class SourceIdentityReference(ABC):
    """Abstract reference to a source artifact.

    This represents an abstract reference to a source artifact, not raw_content,
    in-memory object, or frozen schema. The exact identifier format and schema
    are deferred to later milestones.
    """


class GeneratorIdentityVersion(ABC):
    """Logical component producing a Derived Artifact.

    This may later be deterministic, rule-based, statistical, semantic, or
    LLM-based. No generate() method is defined in M1.
    """


class ProvenanceLineage(ABC):
    """Extensible origin explanation.

    This provides extensible origin explanation that may reference Source,
    Generator, Configuration, etc. Source-origin provenance may exist without
    Generator. No fixed tuple (e.g., source_id + generator_id + timestamp)
    is defined. Persistence schema is deferred.
    """


class CoverageDiagnostics(ABC):
    """Neutral foundation for scope coverage and diagnostic signaling.

    This provides a neutral foundation without severity taxonomy, thresholds,
    or aggregation rules. Concrete representation is deferred.
    """


class DomainResult(ABC):
    """Root for domain-level outcomes.

    This covers domain-level outcomes such as parsed, canonicalized, validated
    results, separate from operational failures.
    """


class OperationalProcessingFailure(ABC):
    """Neutral root for non-domain failures.

    This covers non-domain failures such as parsing, validation, provider,
    policy failures. Concrete categories are deferred.
    """
