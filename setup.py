"""
SupraZone Framework — Spiral Resonance Proof (v3.3)
A physics-inspired, zero-entropy analytical engine for modeling spiral resonance dynamics.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="suprazone-framework",
    version="3.3.0",
    author="Sylwia Miksztal (Sysia)",
    author_email="s.miksztal@gmail.com",
    description="A physics-inspired, zero-entropy analytical engine for modeling spiral resonance dynamics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sysia48/SupraZone-Framework",
    project_urls={
        "Bug Tracker": "https://github.com/sysia48/SupraZone-Framework/issues",
        "Documentation": "https://github.com/sysia48/SupraZone-Framework/blob/main/docs/SupraZone_v3.3.md",
        "Source Code": "https://github.com/sysia48/SupraZone-Framework",
        "IMS White Paper": "https://doi.org/10.5281/zenodo.17252965",
        "Annex II": "https://doi.org/10.5281/zenodo.17799715",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "isort>=5.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "suprazone-configure=configure_user:main",
        ],
    },
    include_package_data=True,
    keywords="resonance physics spiral-dynamics zero-entropy fft signal-processing",
    zip_safe=False,
)
