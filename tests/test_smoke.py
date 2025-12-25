"""Smoke test to verify basic test infrastructure."""


def test_smoke():
    """Basic smoke test that always passes."""
    assert True


def test_imports():
    """Test that core dependencies can be imported."""
    import numpy
    import scipy
    import matplotlib
    import pandas
    
    assert numpy is not None
    assert scipy is not None
    assert matplotlib is not None
    assert pandas is not None
