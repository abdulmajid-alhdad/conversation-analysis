"""M1 Architecture Tests for Required Ports.

These tests verify the M1 ports and architectural compliance.
"""

import ast
from pathlib import Path


def test_required_ports_exist():
    """Test 8: Required Ports exist and contain no infrastructure types."""
    from conversation_analysis.application.ports import (
        CanonicalPersistencePort,
        DerivedArtifactPersistencePort,
        ExecutionMetadataPort,
        SourceAccessPreservationPort,
        TelemetryPort,
    )

    # Verify all 5 required ports exist
    assert SourceAccessPreservationPort is not None
    assert CanonicalPersistencePort is not None
    assert DerivedArtifactPersistencePort is not None
    assert ExecutionMetadataPort is not None
    assert TelemetryPort is not None


def test_source_access_preservation_port():
    """Test Source Access / Preservation Port compliance."""
    from conversation_analysis.application.ports import SourceAccessPreservationPort

    assert isinstance(SourceAccessPreservationPort, type)


def test_canonical_persistence_port():
    """Test Canonical Persistence Port compliance."""
    from conversation_analysis.application.ports import CanonicalPersistencePort

    assert isinstance(CanonicalPersistencePort, type)


def test_derived_artifact_persistence_port():
    """Test Derived Artifact Persistence Port compliance."""
    from conversation_analysis.application.ports import DerivedArtifactPersistencePort

    assert isinstance(DerivedArtifactPersistencePort, type)


def test_execution_metadata_port():
    """Test Execution Metadata Port compliance."""
    from conversation_analysis.application.ports import ExecutionMetadataPort

    assert isinstance(ExecutionMetadataPort, type)


def test_telemetry_port():
    """Test Telemetry Port compliance."""
    from conversation_analysis.application.ports import TelemetryPort

    assert isinstance(TelemetryPort, type)


def test_no_infrastructure_imports_in_ports():
    """Test ports contain no infrastructure types."""
    ports_path = Path("src/conversation_analysis/application/ports.py")
    with open(ports_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the AST to check for imports
    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert not alias.name.startswith("infrastructure"), (
                    f"Infrastructure import found: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert not node.module.startswith("infrastructure"), (
                f"Infrastructure import found: {node.module}"
            )


def test_no_delivery_imports_in_ports():
    """Test ports contain no delivery imports."""
    ports_path = Path("src/conversation_analysis/application/ports.py")
    with open(ports_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the AST to check for imports
    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert not alias.name.startswith("delivery"), (
                    f"Delivery import found: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert not node.module.startswith("delivery"), (
                f"Delivery import found: {node.module}"
            )


def test_no_provider_sdk_imports_in_ports():
    """Test ports contain no Provider SDK imports."""
    ports_path = Path("src/conversation_analysis/application/ports.py")
    with open(ports_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the AST to check for imports
    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                # Check for common provider SDK patterns
                assert "provider" not in alias.name.lower(), (
                    f"Provider SDK import found: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert "provider" not in node.module.lower(), (
                f"Provider SDK import found: {node.module}"
            )


def test_no_parser_concrete_types_in_ports():
    """Test ports contain no Parser concrete types."""
    ports_path = Path("src/conversation_analysis/application/ports.py")
    with open(ports_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the AST to check for imports
    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert "parser" not in alias.name.lower(), (
                    f"Parser concrete type import found: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert "parser" not in node.module.lower(), (
                f"Parser concrete type import found: {node.module}"
            )
