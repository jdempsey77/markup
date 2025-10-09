# Design Phase Agents

## Overview
The Design phase agents help ensure security is built into system architecture and design patterns.

## Agents

### 1. Design Reviewer
**Purpose**: Performs threat modeling and validates security patterns in design documents.

**Capabilities**:
- Automated threat modeling using STRIDE methodology
- Design pattern security analysis
- Architecture review for security anti-patterns
- Trust boundary identification

**Integration Points**:
- Design documentation (Confluence, Notion)
- Architecture diagrams (draw.io, Lucidchart)
- Threat modeling tools

### 2. Cloud/IaC Architect
**Purpose**: Provides reference architectures and guardrails for cloud infrastructure.

**Capabilities**:
- Cloud security best practices
- IaC template validation
- Multi-cloud architecture patterns
- Compliance-ready reference architectures

**Integration Points**:
- AWS, Azure, GCP
- Terraform, CloudFormation
- Architecture repositories

### 3. Abuse Case Writer
**Purpose**: Generates attacker perspective scenarios to identify design weaknesses.

**Capabilities**:
- Attack scenario generation
- Adversarial thinking prompts
- Security test case creation
- Red team perspective analysis

**Integration Points**:
- Test management systems
- Security testing frameworks
- Threat intelligence platforms

## Usage

```python
from phases.design.design_reviewer import DesignReviewer
from phases.design.cloud_iac_architect import CloudIaCArchitect
from phases.design.abuse_case_writer import AbuseCaseWriter

# Design Review
reviewer = DesignReviewer()
threats = reviewer.perform_threat_model(
    architecture_diagram="path/to/diagram.png",
    components=["web_server", "database", "api_gateway"]
)

# Cloud Architecture
architect = CloudIaCArchitect()
recommendations = architect.review_architecture(
    cloud_provider="aws",
    services=["ec2", "rds", "s3"]
)

# Abuse Cases
abuse_writer = AbuseCaseWriter()
scenarios = abuse_writer.generate_abuse_cases(
    feature="user_authentication",
    attack_surface="web_application"
)
```

## Configuration

See `config/design.yaml` for configuration options.

