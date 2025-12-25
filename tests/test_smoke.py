"""
Basic smoke test for SupraZone Framework
"""
import pytest


def test_smoke():
    """Simple smoke test to verify test infrastructure is working"""
    assert True


def test_imports():
    """Test that basic Python imports work"""
    import sys
    assert sys.version_info >= (3, 10)
