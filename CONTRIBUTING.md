# Contributing to SupraZone Framework

Thank you for your interest in contributing to SupraZone Framework! We welcome contributions from the community.

## Opening Issues

- **Bug Reports**: Use the bug report template to describe the issue, including steps to reproduce, expected behavior, and environment details.
- **Feature Requests**: Use the feature request template to propose new functionality, explaining the motivation and proposed solution.

## Code Style

- Follow **PEP 8** style guidelines for Python code.
- Use meaningful variable and function names.
- Add docstrings to functions and classes.
- Keep functions focused and modular.

## Running Tests

To run the test suite locally:

```bash
pip install pytest
pytest -v
```

Ensure all tests pass before submitting a pull request.

## Branch Naming

Use descriptive branch names with prefixes:
- `feature/` - New features
- `fix/` - Bug fixes
- `chore/` - Maintenance tasks
- `docs/` - Documentation updates

Example: `feature/add-spectrum-analysis`

## Commit Messages

Write clear, concise commit messages:
- Use present tense ("Add feature" not "Added feature")
- Start with a verb ("Fix", "Add", "Update", "Remove")
- Keep first line under 72 characters
- Add detailed description if needed

Examples:
```
Add spiral resonance visualization
Fix entropy calculation edge case
Update README with installation instructions
```

## Pull Request Process

1. **Fork and Branch**: Create a branch from `main` for your changes.
2. **Make Changes**: Implement your feature or fix.
3. **Test**: Ensure all tests pass and add new tests for your changes.
4. **Commit**: Use clear commit messages following the guidelines above.
5. **Push**: Push your branch to your fork.
6. **Open PR**: Create a pull request with a clear description of your changes.
7. **Review**: At least one maintainer approval is required.
8. **CI**: All CI checks must pass before merging.

## Code Review

- Be respectful and constructive in code reviews.
- Address all review comments before merging.
- Maintainers will review PRs as soon as possible.

Thank you for contributing!
