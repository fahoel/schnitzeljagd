# Contributing to Schnitzeljagd

Thank you for considering contributing to the Schnitzeljagd scavenger hunt app! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment (see README.md)
4. Create a new branch for your feature or bugfix

```bash
git checkout -b feature/your-feature-name
```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (venv or virtualenv)
- Git

### Setup Steps

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install development dependencies:
```bash
pip install pytest pytest-cov black flake8
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line Length**: Maximum 100 characters
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Use double quotes for strings
- **Imports**: Group by standard library, third-party, and local imports

### Code Formatting

We use Black for automatic code formatting:

```bash
black src/
```

Before committing, always run Black on your code.

### Linting

We use Flake8 for linting:

```bash
flake8 src/ --max-line-length=100
```

Fix any linting errors before submitting a pull request.

## Project Structure

```
src/
├── main.py              # Application entry point
├── ui/                  # UI components
│   ├── __init__.py
│   ├── screens/         # Screen definitions
│   └── widgets/         # Custom widgets
├── map/                 # Map and location functionality
│   ├── __init__.py
│   ├── manager.py       # Map manager
│   └── location_service.py
├── camera/              # Photo capture and upload
│   ├── __init__.py
│   ├── manager.py       # Camera manager
│   └── photo_storage.py
└── utils/               # Utility functions
    ├── __init__.py
    ├── hunt_manager.py
    └── api_client.py
```

## Writing Tests

### Test Structure

- Place tests in the `tests/` directory
- Mirror the source structure in tests
- Name test files with `test_` prefix
- Name test functions with `test_` prefix

Example:
```python
# tests/test_map_manager.py
import pytest
from src.map.manager import MapManager

def test_map_initialization():
    """Test that map initializes with default location."""
    manager = MapManager()
    assert manager.latitude == 52.3759
    assert manager.longitude == 9.7320
```

### Running Tests

Run all tests:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest --cov=src tests/
```

Run specific test:
```bash
pytest tests/test_map_manager.py::test_map_initialization
```

### Test Coverage

- Aim for at least 80% code coverage
- Write tests for new features
- Update tests when modifying existing code

## Making Changes

### Branching Strategy

- `main`: Stable, production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Urgent production fixes

### Commit Messages

Follow conventional commit format:

```
type(scope): brief description

Detailed explanation of what and why.

Fixes #issue-number
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(map): add zoom controls to map view

Add zoom in/out buttons to the map interface for better
user control of the map view.

Fixes #42
```

## Pull Request Process

1. **Update Documentation**: Ensure README and other docs are updated if needed

2. **Add Tests**: Include tests for new functionality

3. **Run Tests**: Ensure all tests pass
```bash
pytest tests/
```

4. **Check Code Quality**:
```bash
black src/
flake8 src/ --max-line-length=100
```

5. **Update NEXT_STEPS.md**: Mark completed items if applicable

6. **Create Pull Request**:
   - Write clear title and description
   - Reference related issues
   - Include screenshots for UI changes
   - Request review from maintainers

7. **Address Review Comments**: Respond to feedback and make necessary changes

8. **Merge**: Once approved, maintainer will merge

## Feature Development Guidelines

### Adding a New Feature

1. **Plan**: Open an issue to discuss the feature
2. **Design**: Document the approach in the issue
3. **Implement**: Write code following our standards
4. **Test**: Add comprehensive tests
5. **Document**: Update relevant documentation
6. **Review**: Submit pull request for review

### UI/UX Considerations

- Follow Material Design guidelines (KivyMD)
- Ensure mobile-friendly touch targets (minimum 48dp)
- Test on multiple screen sizes
- Consider accessibility (color contrast, font sizes)
- Provide visual feedback for user actions

### Performance Considerations

- Optimize image sizes before upload
- Use lazy loading for large lists
- Minimize GPS polling frequency
- Cache API responses when appropriate
- Profile code for performance bottlenecks

## Bug Reports

When reporting bugs, include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Detailed steps to reproduce the issue
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: 
   - OS and version
   - Python version
   - App version
   - Device model (for mobile issues)
6. **Screenshots**: If applicable
7. **Logs**: Relevant error messages or logs

## Feature Requests

When requesting features, include:

1. **Use Case**: Why is this feature needed?
2. **Description**: Detailed description of the feature
3. **Mockups**: UI mockups if applicable
4. **Alternatives**: Other solutions you've considered
5. **Additional Context**: Any other relevant information

## Code Review Guidelines

### For Reviewers

- Be constructive and respectful
- Explain the "why" behind suggestions
- Approve when code meets standards
- Test the changes if possible

### For Authors

- Respond to all comments
- Ask for clarification if needed
- Don't take feedback personally
- Update code based on feedback

## Communication

- **GitHub Issues**: Bug reports, feature requests
- **Pull Requests**: Code changes and discussions
- **Discussions**: General questions and ideas

## Resources

- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [KivyMD Documentation](https://kivymd.readthedocs.io/)
- [Git Commit Message Guidelines](https://www.conventionalcommits.org/)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, feel free to open an issue with the question label.

Thank you for contributing to Schnitzeljagd! 🎯
