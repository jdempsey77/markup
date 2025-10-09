# Quick Start Guide

Get started with the DevSecOps AI Agent Framework in minutes.

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Git

### Install from Source

```bash
# Clone the repository
git clone https://github.com/jdempsey77/markup.git
cd markup

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Install from PyPI (Coming Soon)

```bash
pip install devsecops-ai-agents
```

## Configuration

### 1. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
# Required: AI Provider
OPENAI_API_KEY=sk-your-key-here

# Optional: GitHub Integration
GITHUB_TOKEN=ghp_your-token-here

# Optional: Other Integrations
SNYK_TOKEN=your-snyk-token
SEMGREP_TOKEN=your-semgrep-token
```

### 2. Verify Installation

```bash
# Run example script
python examples/basic_usage.py
```

## Your First Agent

### Example 1: Analyze Security Requirements

```python
from phases.plan.roadmapping_agent import RoadmappingAgent

# Initialize agent
agent = RoadmappingAgent()

# Analyze an epic/user story
result = agent.analyze_epic(
    epic_id="EPIC-123",
    description="Build user authentication with OAuth and MFA",
    project_type="web_app"
)

# View security requirements
for req in result['security_requirements']:
    print(f"{req.priority}: {req.title}")
```

### Example 2: Find Compliance Standards

```python
from phases.plan.policy_scout import PolicyScout

# Initialize agent
scout = PolicyScout()

# Find applicable standards
standards = scout.find_standards(
    industry="fintech",
    data_types=["PII", "payment_card_data"],
    regions=["US", "EU"]
)

# View standards
for standard in standards:
    print(f"{standard.framework} - {standard.priority}")
```

### Example 3: Run a Complete Phase

```python
from pipeline import DevSecOpsPipeline, Phase

# Initialize pipeline
pipeline = DevSecOpsPipeline()

# Run Plan phase
results = pipeline.run_phase(
    Phase.PLAN,
    epic_id="EPIC-456",
    description="Healthcare patient portal",
    industry="healthcare",
    data_types=["PHI", "PII"]
)

print(f"Found {len(results)} agent results")
```

## Common Use Cases

### Use Case 1: PR Security Review

```python
# Code review on pull request
from phases.build.code_reviewer import CodeReviewer

reviewer = CodeReviewer()
findings = reviewer.review_pull_request(
    repo="owner/repo",
    pr_number=42
)

# Post results as PR comment
reviewer.post_comment(findings)
```

### Use Case 2: Dependency Scanning

```python
# Scan dependencies for vulnerabilities
from phases.build.supply_chain_sentinel import SupplyChainSentinel

sentinel = SupplyChainSentinel()
vulnerabilities = sentinel.scan_dependencies(
    manifest_file="package.json"
)

print(f"Found {len(vulnerabilities)} vulnerabilities")
```

### Use Case 3: API Security Testing

```python
# Dynamic API testing
from phases.test.dast_api_fuzzer import DASTAPIFuzzer

fuzzer = DASTAPIFuzzer()
issues = fuzzer.test_api(
    api_url="https://api.example.com",
    spec_file="openapi.yaml"
)
```

## Integration with CI/CD

### GitHub Actions

Add to `.github/workflows/security.yml`:

```yaml
name: Security Scan

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install DevSecOps Framework
        run: pip install devsecops-ai-agents
      
      - name: Run Security Scan
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          devsecops-agent --phase build --output results.json
```

### GitLab CI

Add to `.gitlab-ci.yml`:

```yaml
security_scan:
  image: python:3.11
  script:
    - pip install devsecops-ai-agents
    - devsecops-agent --phase build --output results.json
  artifacts:
    reports:
      security: results.json
```

## CLI Usage

### Run Specific Phase

```bash
# Run build phase
devsecops-agent --phase build

# Run with specific agent
devsecops-agent --phase build --agent code-reviewer

# Specify output format
devsecops-agent --phase test --output-format sarif --output-file results.sarif
```

### Configuration Override

```bash
# Use custom config
devsecops-agent --config custom-config.yaml

# Override specific settings
devsecops-agent --set ai.provider=anthropic --set logging.level=DEBUG
```

## Next Steps

1. **Explore Documentation**
   - [Architecture Guide](architecture.md)
   - [Configuration Reference](configuration.md)
   - [API Documentation](api.md)

2. **Try Examples**
   - Browse `examples/` directory
   - Run example scripts
   - Customize for your needs

3. **Integrate with Your Workflow**
   - Add to CI/CD pipeline
   - Configure for your tech stack
   - Customize agent behavior

4. **Contribute**
   - See [CONTRIBUTING.md](../CONTRIBUTING.md)
   - Report issues
   - Submit improvements

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'phases'`
```bash
# Solution: Install in development mode
pip install -e .
```

**Issue**: `Authentication Error` from AI provider
```bash
# Solution: Check your API key in .env
echo $OPENAI_API_KEY  # Should output your key
```

**Issue**: `Permission Denied` errors
```bash
# Solution: Check file permissions
chmod +x scripts/*.sh
```

## Getting Help

- **Documentation**: Check the [docs/](.) directory
- **Examples**: See [examples/](../examples/) directory
- **Issues**: [GitHub Issues](https://github.com/jdempsey77/markup/issues)
- **Discussions**: [GitHub Discussions](https://github.com/jdempsey77/markup/discussions)

## What's Next?

Now that you have the basics working:

1. ✅ Customize configuration for your environment
2. ✅ Integrate with your CI/CD pipeline
3. ✅ Explore advanced agent features
4. ✅ Set up notifications and reporting
5. ✅ Contribute improvements back to the project

Happy Secure Coding! 🔒🚀

