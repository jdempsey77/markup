# Build Phase Agents

## Overview
The Build phase agents provide continuous security analysis during code development.

## Agents

### 1. Code Reviewer (AppSec)
**Purpose**: Performs SAST scanning, secret detection, linting, and provides PR recommendations.

**Capabilities**:
- Static application security testing (SAST)
- Secret and credential detection
- Code quality and security linting
- Pull request security reviews
- Secure coding recommendations

**Integration Points**:
- GitHub, GitLab, Bitbucket
- Semgrep, Bandit, ESLint
- SonarQube, CodeQL

### 2. Supply Chain Sentinel
**Purpose**: Software composition analysis, license checking, and SBOM generation.

**Capabilities**:
- Dependency vulnerability scanning (SCA)
- License compliance checking
- SBOM generation and management
- Transitive dependency analysis
- Known vulnerability detection

**Integration Points**:
- npm, pip, maven, gradle
- Snyk, Dependabot
- CycloneDX, SPDX

### 3. IaC Linter
**Purpose**: Security checks for Infrastructure as Code (Terraform, Kubernetes, Docker).

**Capabilities**:
- Terraform security scanning
- Kubernetes manifest validation
- Docker image security analysis
- Cloud resource misconfiguration detection
- Policy-as-code enforcement

**Integration Points**:
- Terraform, CloudFormation
- Kubernetes, Helm
- Docker, container registries
- Checkov, tfsec, trivy

## Usage

```python
from phases.build.code_reviewer import CodeReviewer
from phases.build.supply_chain_sentinel import SupplyChainSentinel
from phases.build.iac_linter import IaCLinter

# Code Review
reviewer = CodeReviewer()
findings = reviewer.review_pull_request(
    repo="owner/repo",
    pr_number=42
)

# Supply Chain Analysis
sentinel = SupplyChainSentinel()
vulnerabilities = sentinel.scan_dependencies(
    manifest_file="package.json"
)

# IaC Scanning
linter = IaCLinter()
issues = linter.scan_terraform(
    terraform_dir="infrastructure/"
)
```

## Configuration

See `config/build.yaml` for configuration options.

