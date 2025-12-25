# Contributing to SupraZone Framework

Thank you for your interest in contributing to SupraZone Framework! We welcome contributions from the community.

## How to Contribute

### Opening Issues

- **Bug Reports**: Use the bug report template to describe the issue, including steps to reproduce, expected behavior, and your environment.
- **Feature Requests**: Use the feature request template to propose new features or enhancements.
- **Questions**: For general questions, please open a discussion or issue with the "question" label.

### Code Style

- Follow **PEP 8** style guidelines for Python code.
- Use meaningful variable and function names.
- Add docstrings to functions and classes.
- Keep functions focused and concise.
- Use type hints where appropriate.

### Running Tests Locally

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest
   ```

2. Run the test suite:
   ```bash
   pytest
   ```

3. Ensure all tests pass before submitting a pull request.

### Branch Naming

Use descriptive branch names with the following prefixes:
- `feature/` - for new features
- `fix/` - for bug fixes
- `chore/` - for maintenance tasks
- `docs/` - for documentation updates

Example: `feature/add-spectral-analysis` or `fix/memory-leak-in-fft`

### Commit Message Conventions

Follow conventional commit format:
- `feat:` - new feature
- `fix:` - bug fix
- `docs:` - documentation changes
- `style:` - code style changes (formatting, etc.)
- `refactor:` - code refactoring
- `test:` - adding or updating tests
- `chore:` - maintenance tasks

Example: `feat: add FFT analysis for resonance patterns`

### Pull Request Process

1. Fork the repository and create your branch from `main`.
2. Make your changes, ensuring code quality and test coverage.
3. Run tests locally to verify your changes.
4. Update documentation if needed.
5. Submit a pull request with a clear description of changes.
6. Ensure CI checks pass.
7. **At least one maintainer approval is required** before merging.
8. **All CI tests must pass** before a PR can be merged.

### Code Review

- Be respectful and constructive in code reviews.
- Address review comments promptly.
- Maintainers may request changes before approving.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/sysia48/SupraZone-Framework.git
cd SupraZone-Framework

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest

# Run tests
pytest
```

## Questions?

Feel free to open an issue or reach out to the maintainers if you have any questions.

Thank you for contributing! 🌀
