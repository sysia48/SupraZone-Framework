# Contributing to SupraZone Framework

Thank you for your interest in contributing to SupraZone Framework! We welcome contributions from the community.

## Opening Issues

If you find a bug or have a feature request, please open an issue on GitHub. When opening an issue, please:

- Provide a clear and descriptive title
- Include steps to reproduce the issue (for bugs)
- Describe the expected behavior and actual behavior
- Include your Python version and operating system

## Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style. Please ensure your code adheres to these guidelines:

- Use 4 spaces for indentation (no tabs)
- Keep lines under 79 characters where possible
- Use descriptive variable names
- Add docstrings to functions and classes

## Running Tests Locally

To run tests locally, ensure you have installed the development dependencies:

```bash
pip install -r requirements.txt
pip install pytest
```

Then run the test suite:

```bash
pytest
```

Make sure all tests pass before submitting a pull request.

## Branch Naming

Please use the following branch naming conventions:

- `feature/ISSUE-<number>-<short-description>` for new features
- `bugfix/ISSUE-<number>-<short-description>` for bug fixes
- `chore/<short-description>` for maintenance tasks
- `docs/<short-description>` for documentation updates

Example: `feature/ISSUE-42-add-new-resonance-model`

## Pull Request Process

1. Fork the repository and create your branch from `main`
2. Make your changes and ensure tests pass
3. Update documentation if needed
4. Write clear, concise commit messages
5. Submit a pull request with a description of your changes

## Code Review

All pull requests will be reviewed by maintainers. Please be patient and address any feedback or requested changes.

## License

By contributing to SupraZone Framework, you agree that your contributions will be licensed under the MIT License.
