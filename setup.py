#!/usr/bin/env python3
# =========================================================
#  SETUP.PY — SupraZone Framework Package Configuration
# =========================================================

"""
Setup configuration for SupraZone Framework.

This file enables the package to be installed via pip and
published to PyPI (Python Package Index).
"""

from setuptools import setup, find_packages
import os

# Read the long description from README
def read_long_description():
    """Read README.md for PyPI long description."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Read requirements
def read_requirements():
    """Read requirements.txt for dependencies."""
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    # Package metadata
    name='suprazone-framework',
    version='3.3.0',
    description='Physics-inspired zero-entropy analytical engine for spiral resonance dynamics',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    
    # Author information
    author='Sylwia Miksztal (Sysia)',
    author_email='s.miksztal@gmail.com',
    
    # Project URLs
    url='https://github.com/sysia48/SupraZone-Framework',
    project_urls={
        'Documentation': 'https://github.com/sysia48/SupraZone-Framework/blob/main/docs/SupraZone_v3.3.md',
        'Source': 'https://github.com/sysia48/SupraZone-Framework',
        'Tracker': 'https://github.com/sysia48/SupraZone-Framework/issues',
        'IMS White Paper': 'https://doi.org/10.5281/zenodo.17252965',
        'Spiral Resonance Proof': 'https://doi.org/10.5281/zenodo.17799715',
    },
    
    # License
    license='MIT',
    
    # Package discovery
    packages=['suprazone'],
    package_dir={'suprazone': 'suprazone'},
    
    # Include additional files
    include_package_data=True,
    
    # Dependencies
    install_requires=read_requirements(),
    
    # Python version requirement
    python_requires='>=3.7',
    
    # Package classifiers for PyPI
    classifiers=[
        # Development status
        'Development Status :: 4 - Beta',
        
        # Intended audience
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        
        # Topic classification
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        
        # License
        'License :: OSI Approved :: MIT License',
        
        # Python versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        
        # Operating systems
        'Operating System :: OS Independent',
        
        # Additional classifiers
        'Natural Language :: English',
    ],
    
    # Keywords for discovery
    keywords=[
        'physics',
        'resonance',
        'signal-processing',
        'fourier-analysis',
        'fft',
        'entropy',
        'dynamics',
        'simulation',
        'visualization',
        'scientific-computing',
    ],
    
    # Entry points for command-line scripts
    entry_points={
        'console_scripts': [
            'suprazone-configure=suprazone.configure_user:main',
        ],
    },
    
    # Additional metadata
    zip_safe=False,
)
