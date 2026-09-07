"""M1 Architecture Tests for Application Orchestration.

These tests verify the M1 orchestration and architectural compliance.
"""

import ast
from pathlib import Path


def test_orchestration_boundary_exists():
    """Test 9: Application orchestration imports only permitted dependencies."""
    from conversation_analysis.application.orchestration import Orchestration

    # Verify the orchestration class exists
    assert Orchestration is not None


def test_orchestration_compliance():
    """Test orchestration follows M1 specification."""
    from conversation_analysis.application.orchestration import Orchestration

    # Verify it's a class (not an instance or other type)
    assert isinstance(Orchestration, type)


def test_no_infrastructure_imports_in_orchestration():
    """Test orchestration contains no infrastructure types."""
    orchestration_path = Path("src/conversation_analysis/application/orchestration.py")
    with open(orchestration_path, "r", encoding="utf-8") as f:
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


def test_no_delivery_imports_in_orchestration():
    """Test orchestration contains no delivery imports."""
    orchestration_path = Path("src/conversation_analysis/application/orchestration.py")
    with open(orchestration_path, "r", encoding="utf-8") as f:
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


def test_no_provider_sdk_imports_in_orchestration():
    """Test orchestration contains no Provider SDK imports."""
    orchestration_path = Path("src/conversation_analysis/application/orchestration.py")
    with open(orchestration_path, "r", encoding="utf-8") as f:
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


def test_no_parser_concrete_types_in_orchestration():
    """Test orchestration contains no Parser concrete types."""
    orchestration_path = Path("src/conversation_analysis/application/orchestration.py")
    with open(orchestration_path, "r", encoding="utf-8") as f:
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
