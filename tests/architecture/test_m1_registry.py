"""M1 Architecture Tests for Contract & Capability Registry.

These tests verify the M1 registry abstraction and architectural compliance.
"""

import ast
from pathlib import Path


def test_registry_abstraction_exists():
    """Test 7: Contract & Capability Registry resolution abstraction."""
    from conversation_analysis.application.registry import ContractCapabilityRegistry

    # Verify the registry class exists
    assert ContractCapabilityRegistry is not None


def test_registry_abstraction_compliance():
    """Test registry follows M1 specification."""
    from conversation_analysis.application.registry import ContractCapabilityRegistry

    # Verify it's a class (not an instance or other type)
    assert isinstance(ContractCapabilityRegistry, type)


def test_no_infrastructure_imports_in_registry():
    """Test registry contains no infrastructure types."""
    registry_path = Path("src/conversation_analysis/application/registry.py")
    with open(registry_path, "r", encoding="utf-8") as f:
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


def test_no_delivery_imports_in_registry():
    """Test registry contains no delivery imports."""
    registry_path = Path("src/conversation_analysis/application/registry.py")
    with open(registry_path, "r", encoding="utf-8") as f:
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


def test_no_provider_sdk_imports_in_registry():
    """Test registry contains no Provider SDK imports."""
    registry_path = Path("src/conversation_analysis/application/registry.py")
    with open(registry_path, "r", encoding="utf-8") as f:
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


def test_no_parser_concrete_types_in_registry():
    """Test registry contains no Parser concrete types."""
    registry_path = Path("src/conversation_analysis/application/registry.py")
    with open(registry_path, "r", encoding="utf-8") as f:
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
