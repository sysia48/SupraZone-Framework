# Contributing to SupraZone Framework

Thank you for your interest in contributing to SupraZone Framework! This document provides guidelines and instructions for contributing.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs
- Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Search existing issues to avoid duplicates
- Include detailed steps to reproduce the issue
- Provide environment details (OS, Python version, etc.)

### Suggesting Features
- Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md)
- Clearly describe the problem and proposed solution
- Explain the use case and benefits

### Opening Pull Requests
1. Fork the repository
2. Create a feature branch from `main` using the naming convention:
   - `feature/description` for new features
   - `fix/description` for bug fixes
   - `chore/description` for maintenance tasks
   - `docs/description` for documentation updates
3. Make your changes following our code style
4. Write or update tests as needed
5. Ensure all tests pass locally
6. Submit a pull request with a clear description

## Development Setup

### Prerequisites
- Python 3.10 or 3.11
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/sysia48/SupraZone-Framework.git
cd SupraZone-Framework

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest
```

## Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Comment complex logic when necessary

## Testing

### Running Tests Locally
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_smoke.py
```

### Writing Tests
- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Name test functions with `test_` prefix
- Use descriptive test names that explain what is being tested
- Include both positive and negative test cases

## Submitting Changes

### Before Submitting
1. **Run tests**: Ensure all tests pass
   ```bash
   pytest -v
   ```

2. **Check your code**: Review your changes for:
   - Code style consistency
   - Proper documentation
   - Test coverage
   - No unnecessary files or changes

3. **Update documentation**: If your changes affect usage or API, update relevant documentation

### Pull Request Process
1. **Create a clear PR title**: Use conventional commit format
   - `feat: add new feature`
   - `fix: resolve bug in X`
   - `docs: update README`
   - `chore: update dependencies`

2. **Write a detailed description**:
   - Explain what changes were made and why
   - Reference related issues (e.g., "Closes #123")
   - Include any breaking changes
   - Add screenshots for UI changes

3. **Request review**: At least one approval from a repository maintainer is required

4. **Pass CI checks**: All GitHub Actions workflows must pass

5. **Respond to feedback**: Address reviewer comments promptly

### Branch Naming Convention
- `feature/your-feature-name` - New features
- `fix/issue-description` - Bug fixes
- `docs/what-changed` - Documentation updates
- `chore/task-description` - Maintenance tasks

## Review Process

- Pull requests require at least **one approval** from a repository maintainer
- All CI checks must pass before merging
- Maintainers may request changes or provide feedback
- Be patient and responsive during the review process

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Reach out to the maintainers

Thank you for contributing to SupraZone Framework! 🌀
