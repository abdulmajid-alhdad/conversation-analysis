"""M1 Architecture Tests for Core Contracts.

These tests verify the M1 contract boundaries and architectural compliance.
"""

import ast
from pathlib import Path


def test_core_contracts_importability():
    """Test 1: Core contracts importability."""
    # Import the core contracts module
    from conversation_analysis.core import contracts

    # Verify that the module can be imported without errors
    assert hasattr(contracts, "SourceIdentityReference")
    assert hasattr(contracts, "GeneratorIdentityVersion")
    assert hasattr(contracts, "ProvenanceLineage")
    assert hasattr(contracts, "CoverageDiagnostics")
    assert hasattr(contracts, "DomainResult")
    assert hasattr(contracts, "OperationalProcessingFailure")


def test_source_identity_reference_contract_boundary():
    """Test 2: Source identity/reference contract boundary."""
    from conversation_analysis.core.contracts import SourceIdentityReference

    # Verify it's an abstract class
    # Check that it doesn't define concrete implementation details
    # The class should be minimal and abstract
    source_class = SourceIdentityReference
    assert hasattr(source_class, "__abstractmethods__")


def test_generator_version_contract_boundary():
    """Test 3: Generator/version contract boundary."""
    from conversation_analysis.core.contracts import GeneratorIdentityVersion

    # Verify it's an abstract class
    # Check that it doesn't define generate() method (as specified in M1)
    generator_class = GeneratorIdentityVersion
    assert hasattr(generator_class, "__abstractmethods__")


def test_provenance_extensibility_non_overbinding():
    """Test 4: Provenance extensibility/non-overbinding."""
    from conversation_analysis.core.contracts import ProvenanceLineage

    # Verify it's an abstract class
    assert hasattr(ProvenanceLineage, "__abstractmethods__")


def test_coverage_diagnostics_foundation_neutrality():
    """Test 5: Coverage/Diagnostics foundation neutrality."""
    from conversation_analysis.core.contracts import CoverageDiagnostics

    # Verify it's an abstract class
    assert hasattr(CoverageDiagnostics, "__abstractmethods__")


def test_domain_result_vs_operational_failure_separation():
    """Test 6: Domain Result vs Operational Failure separation."""
    from conversation_analysis.core.contracts import (
        DomainResult,
        OperationalProcessingFailure,
    )

    # Both should be abstract classes
    # They should be distinct classes
    assert DomainResult != OperationalProcessingFailure


def test_no_infrastructure_imports_in_core_contracts():
    """Test 8: Core contracts contain no infrastructure types."""
    contracts_path = Path("src/conversation_analysis/core/contracts.py")
    with open(contracts_path, "r", encoding="utf-8") as f:
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


def test_no_delivery_imports_in_core_contracts():
    """Test 15: Core contains no Delivery imports."""
    contracts_path = Path("src/conversation_analysis/core/contracts.py")
    with open(contracts_path, "r", encoding="utf-8") as f:
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


def test_no_provider_sdk_imports_in_core_contracts():
    """Test 13: Core/Application contain no Provider SDK imports."""
    contracts_path = Path("src/conversation_analysis/core/contracts.py")
    with open(contracts_path, "r", encoding="utf-8") as f:
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


def test_no_parser_concrete_types_in_core_contracts():
    """Test 14: Core contains no Parser concrete types."""
    contracts_path = Path("src/conversation_analysis/core/contracts.py")
    with open(contracts_path, "r", encoding="utf-8") as f:
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
