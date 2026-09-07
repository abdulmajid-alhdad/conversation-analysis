"""Required application ports for the Arabic Conversation Analysis Engine.

This module defines the five required ports that serve as substrates for
future milestones without specifying concrete implementations or behaviors.
"""


class SourceAccessPreservationPort:
    """Substrate for M2 Source Access and Preservation.

    May support: immutable source revision, metadata read, stream content,
    bounded/range reads, integrity verification, reference resolution.
    Exact methods/types are deferred to later milestones.
    """


class CanonicalPersistencePort:
    """Substrate for M4 Canonical Persistence.

    This serves as the substrate for canonical data persistence without
    defining the Canonical implementation or storage schema in M1.
    """


class DerivedArtifactPersistencePort:
    """Substrate for M6 Derived Artifact Persistence.

    This serves as the substrate for derived artifact persistence without
    defining the Artifact Envelope implementation in M1.
    """


class ExecutionMetadataPort:
    """Substrate for M6 Execution Metadata.

    This serves as the substrate for execution metadata without defining
    AnalysisRun / ExecutionAttempt schema in M1.
    """


class TelemetryPort:
    """Substrate for diagnostics/operations across M2-M6.

    This serves as the substrate for telemetry without defining backend
    or event schema in M1.
    """
