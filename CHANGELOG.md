# Changelog

All notable changes to the SupraZone Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.3.0] - 2025-12-25

### Added
- Complete project restructuring for PyPI compatibility
- Added `setup.py` for package distribution
- Added `pyproject.toml` for modern Python packaging
- Added `MANIFEST.in` for package file inclusion
- Added comprehensive CI/CD workflows:
  - Automated testing workflow
  - Code linting and quality checks
  - PyPI publishing workflow
- Added example directory with practical usage examples:
  - Basic usage example
  - Advanced usage example
  - Visualization examples
  - Jupyter notebook example
- Added comprehensive testing infrastructure:
  - Unit tests for core modules
  - Integration tests
  - pytest configuration
- Added developer documentation:
  - CONTRIBUTING.md with contribution guidelines
  - CODE_OF_CONDUCT.md
  - DEVELOPMENT.md with setup instructions
  - Issue templates for bug reports and feature requests
  - Pull request template
- Added LICENSE file (MIT)
- Added CHANGELOG.md

### Changed
- Enhanced README.md with CI/CD status badges
- Updated .gitignore with comprehensive exclusion rules
- Improved inline API documentation

### Fixed
- None

## [3.2.0] - 2025-10-10

### Added
- User account settings feature for customizable attribution
- Interactive configuration script (`configure_user.py`)
- `user_settings.json` for storing user preferences
- User settings module in `src/user_settings.py`

### Changed
- Updated main framework to use user settings for output attribution
- Enhanced README with user configuration instructions

## [3.1.0] - Initial Release

### Added
- Core spiral resonance proof framework
- FFT spectral analysis
- Energy heatmap visualization
- CSV data export functionality
- Modular architecture with separate components:
  - `parameters.py` - Parameter definitions
  - `energy.py` - Energy calculations
  - `fft_analysis.py` - FFT analysis
  - `heatmap.py` - Visualization
  - `user_settings.py` - User configuration
- Documentation in `docs/SupraZone_v3.3.md`

[3.3.0]: https://github.com/sysia48/SupraZone-Framework/compare/v3.2.0...v3.3.0
[3.2.0]: https://github.com/sysia48/SupraZone-Framework/compare/v3.1.0...v3.2.0
[3.1.0]: https://github.com/sysia48/SupraZone-Framework/releases/tag/v3.1.0
