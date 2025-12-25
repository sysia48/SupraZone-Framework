# Contributing to SupraZone Framework

Thank you for your interest in contributing to SupraZone Framework! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Code Contributions](#code-contributions)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what you expected**
- **Include screenshots or code samples if applicable**
- **Include your environment details** (OS, Python version, package versions)

Use the bug report template when creating a new issue.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **Include examples of how the enhancement would be used**

Use the feature request template when creating a new issue.

### Code Contributions

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** if you've added code that should be tested
4. **Ensure the test suite passes**
5. **Make sure your code lints**
6. **Write clear commit messages**
7. **Submit a pull request**

## Development Setup

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed setup instructions.

Quick start:

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/SupraZone-Framework.git
cd SupraZone-Framework

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e ".[dev]"

# Run tests
pytest
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use [Black](https://github.com/psf/black) for code formatting (line length: 100)
- Use [isort](https://github.com/PyCQA/isort) for import sorting
- Use [flake8](https://flake8.pycqa.org/) for linting

Run formatters and linters:

```bash
# Format code
black .
isort .

# Check code quality
flake8
```

### Documentation

- Use docstrings for all public modules, functions, classes, and methods
- Follow [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings
- Keep documentation up to date with code changes
- Add inline comments for complex logic

### Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 72 characters
- Reference issues and pull requests when applicable

Examples:
```
Add FFT analysis for resonance patterns
Fix energy calculation in edge cases
Update README with installation instructions
```

## Pull Request Process

1. **Update documentation** if you've changed APIs or added features
2. **Update CHANGELOG.md** with a note describing your changes
3. **Ensure all tests pass** and add new tests for new functionality
4. **Update the README.md** if you've added functionality
5. **Request review** from maintainers
6. **Address review feedback** promptly

### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Code is commented, particularly in complex areas
- [ ] Documentation updated (if applicable)
- [ ] Tests added/updated (if applicable)
- [ ] All tests pass locally
- [ ] CHANGELOG.md updated
- [ ] No new warnings introduced

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_parameters.py

# Run specific test
pytest tests/test_parameters.py::test_parameter_ranges
```

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names that explain what is being tested
- Include both positive and negative test cases
- Test edge cases and error conditions
- Aim for high test coverage (>80%)

Example test structure:

```python
def test_feature_description():
    """Test that feature works as expected."""
    # Arrange
    input_data = prepare_test_data()
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result == expected_output
```

## Questions?

Feel free to open an issue with your question or reach out to the maintainers:

- **Sylwia Miksztal (Sysia)** - s.miksztal@gmail.com

## Recognition

Contributors will be recognized in the project README and release notes. Thank you for helping make SupraZone Framework better!
