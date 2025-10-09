# Plan Phase Agents

## Overview
The Plan phase agents help identify security requirements and compliance needs early in the development lifecycle.

## Agents

### 1. Roadmapping Agent
**Purpose**: Identifies security requirements and provides risk hints during project planning.

**Capabilities**:
- Analyzes project requirements for security implications
- Suggests security controls based on project type
- Identifies regulatory compliance requirements
- Provides risk assessment early in planning

**Integration Points**:
- Jira/Linear for epic and story analysis
- Confluence for documentation
- Compliance databases

### 2. Policy Scout
**Purpose**: Looks up compliance baselines and security standards applicable to the project.

**Capabilities**:
- Identifies relevant security standards (ISO 27001, SOC 2, NIST, etc.)
- Suggests industry-specific compliance requirements
- Provides baseline security policies
- Maps controls to frameworks

**Integration Points**:
- Compliance management systems
- Policy repositories
- Standards databases

## Usage

```python
from phases.plan.roadmapping_agent import RoadmappingAgent
from phases.plan.policy_scout import PolicyScout

# Roadmapping Agent
roadmap_agent = RoadmappingAgent()
security_reqs = roadmap_agent.analyze_epic(
    epic_id="EPIC-123",
    description="Build payment processing system"
)

# Policy Scout
policy_agent = PolicyScout()
applicable_standards = policy_agent.find_standards(
    industry="fintech",
    data_types=["PII", "payment_card_data"]
)
```

## Configuration

See `config/plan.yaml` for configuration options.

