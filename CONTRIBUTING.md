# Contributing to DevSecOps AI Agent Framework

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🌟 Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional, for testing containerized agents)
- API keys for AI services (OpenAI, Anthropic, etc.)

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/jdempsey77/markup.git
   cd markup
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run Tests**
   ```bash
   pytest tests/
   ```

## 🔧 Development Workflow

### Branching Strategy

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes

### Making Changes

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write clean, documented code
   - Follow Python PEP 8 style guide
   - Add type hints where appropriate
   - Update tests as needed

3. **Run Quality Checks**
   ```bash
   # Format code
   black phases/
   
   # Sort imports
   isort phases/
   
   # Lint
   flake8 phases/
   pylint phases/
   
   # Type check
   mypy phases/
   
   # Run tests
   pytest tests/ -v --cov
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

   Use conventional commit messages:
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `test:` - Test additions/changes
   - `refactor:` - Code refactoring
   - `chore:` - Maintenance tasks

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

## 📝 Code Standards

### Python Style

- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use docstrings for all public functions and classes

**Example:**

```python
from typing import List, Optional
from pydantic import BaseModel


class SecurityFinding(BaseModel):
    """Model for security findings."""
    
    severity: str
    description: str
    file_path: Optional[str] = None


def analyze_code(file_path: str, rules: List[str]) -> List[SecurityFinding]:
    """
    Analyze code file for security issues.
    
    Args:
        file_path: Path to the file to analyze
        rules: List of security rules to apply
        
    Returns:
        List of security findings
        
    Raises:
        FileNotFoundError: If file_path doesn't exist
    """
    # Implementation
    pass
```

### Documentation

- All public APIs must have docstrings
- Update README.md for significant changes
- Add examples for new features
- Keep documentation in sync with code

### Testing

- Write unit tests for all new code
- Aim for >80% code coverage
- Include integration tests where appropriate
- Test both success and failure cases

**Test Example:**

```python
import pytest
from phases.plan.roadmapping_agent import RoadmappingAgent


def test_roadmapping_agent_identifies_auth_requirements():
    """Test that roadmapping agent identifies authentication requirements."""
    agent = RoadmappingAgent()
    
    result = agent.analyze_epic(
        epic_id="TEST-123",
        description="Build user login system with OAuth"
    )
    
    assert len(result['security_requirements']) > 0
    assert any('authentication' in req.category.lower() 
               for req in result['security_requirements'])


def test_roadmapping_agent_handles_empty_description():
    """Test agent handles empty epic descriptions gracefully."""
    agent = RoadmappingAgent()
    
    result = agent.analyze_epic(
        epic_id="TEST-124",
        description=""
    )
    
    assert result is not None
    assert 'security_requirements' in result
```

## 🏗️ Project Structure

```
markup/
├── phases/              # Phase-specific agents
│   ├── 01-plan/
│   ├── 02-design/
│   ├── 03-build/
│   ├── 04-test/
│   ├── 05-release/
│   ├── 06-deploy/
│   ├── 07-operate/
│   └── 08-retire/
├── shared/              # Shared utilities
│   ├── models/          # Pydantic models
│   ├── utils/           # Helper functions
│   └── integrations/    # External service integrations
├── config/              # Configuration files
├── docs/                # Documentation
├── examples/            # Example usage
├── tests/               # Test suite
└── scripts/             # Utility scripts
```

## 🤖 Adding a New Agent

1. **Choose the Phase** - Determine which SDLC phase your agent belongs to

2. **Create Agent File** - Create `phases/{phase}/your_agent.py`

3. **Implement Agent Class**
   ```python
   from typing import Dict, Optional
   
   class YourAgent:
       """Your agent description."""
       
       def __init__(self, config_path: Optional[str] = None):
           """Initialize agent."""
           self.config = self._load_config(config_path)
       
       def analyze(self, input_data: Dict) -> Dict:
           """Main agent logic."""
           pass
   ```

4. **Add Tests** - Create `tests/test_{phase}/test_your_agent.py`

5. **Update Documentation** - Update the phase README

6. **Add Example** - Create usage example in `examples/`

## 🔍 Review Process

### Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages follow conventions
- [ ] No secrets or credentials in code
- [ ] CHANGELOG.md updated (for significant changes)

### Review Criteria

1. **Functionality** - Does it work as intended?
2. **Security** - Are there any security concerns?
3. **Performance** - Is it efficient?
4. **Maintainability** - Is it readable and maintainable?
5. **Testing** - Are tests adequate?
6. **Documentation** - Is it well documented?

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, include:

- **Description** - Clear description of the issue
- **Steps to Reproduce** - How to reproduce the bug
- **Expected Behavior** - What should happen
- **Actual Behavior** - What actually happens
- **Environment** - OS, Python version, relevant configurations
- **Logs** - Any relevant error messages or logs

### Feature Requests

When requesting features:

- **Use Case** - Why is this feature needed?
- **Proposed Solution** - How should it work?
- **Alternatives** - Other solutions you've considered
- **Impact** - Who would benefit from this?

## 📋 Coding Guidelines

### Security Best Practices

- Never commit secrets or API keys
- Validate all user inputs
- Use parameterized queries for databases
- Implement proper error handling
- Log security-relevant events
- Follow principle of least privilege

### Performance Considerations

- Avoid unnecessary API calls
- Implement caching where appropriate
- Use async operations for I/O-bound tasks
- Profile code for bottlenecks
- Consider memory usage for large datasets

### Error Handling

```python
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def safe_operation(data: str) -> Optional[dict]:
    """Perform operation with proper error handling."""
    try:
        result = risky_operation(data)
        return result
    except ValueError as e:
        logger.error(f"Invalid input data: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise
```

## 🎯 Areas for Contribution

We especially welcome contributions in:

- **New Agents** - Additional security agents for any phase
- **Integrations** - Connections to security tools and platforms
- **AI Models** - Improved prompts and model integrations
- **Documentation** - Tutorials, guides, and examples
- **Testing** - Improved test coverage and test frameworks
- **Performance** - Optimization and efficiency improvements

## 📞 Getting Help

- **Documentation**: Check the [docs/](docs/) directory
- **Discussions**: Use [GitHub Discussions](https://github.com/jdempsey77/markup/discussions)
- **Issues**: Search [existing issues](https://github.com/jdempsey77/markup/issues)
- **Chat**: Join our community chat (coming soon)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to making DevSecOps better for everyone! 🚀

