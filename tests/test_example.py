"""Tests for the example module."""

import pytest
from suprazone import example


def test_hello():
    """Test the hello function."""
    result = example.hello()
    assert isinstance(result, str)
    assert "Hello" in result
    assert "SupraZone" in result


def test_add():
    """Test the add function."""
    assert example.add(2, 3) == 5
    assert example.add(-1, 1) == 0
    assert example.add(0, 0) == 0


def test_add_floats():
    """Test the add function with floats."""
    result = example.add(1.5, 2.5)
    assert result == 4.0
