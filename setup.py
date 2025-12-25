#!/usr/bin/env python
"""Setup script for SupraZone Framework."""

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="suprazone-framework",
        version="0.0.1",
        packages=find_packages(where="."),
        package_dir={"": "."},
    )
