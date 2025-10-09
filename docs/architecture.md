# Architecture Guide

## Overview

The DevSecOps AI Agent Framework is designed as a modular, extensible system that integrates security practices across the entire Software Development Lifecycle (SDLC).

## Core Principles

### 1. **Shift-Left Security**
Security is integrated early in the development process, starting from the planning phase.

### 2. **AI-Powered Automation**
Leverages large language models (LLMs) and machine learning to provide intelligent security analysis and recommendations.

### 3. **Modular Design**
Each agent is independent and can be used standalone or as part of the complete pipeline.

### 4. **Integration-First**
Designed to integrate seamlessly with existing development tools and workflows.

### 5. **Feedback Loops**
Insights from later phases inform earlier phases, creating a continuous improvement cycle.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface Layer                     │
│  (CLI, API, Web Dashboard, IDE Plugins, CI/CD Integrations) │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  Orchestration Layer                         │
│         (Pipeline Manager, Agent Coordinator)                │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    Agent Layer (8 Phases)                    │
├──────────────────────────────────────────────────────────────┤
│  Plan    │ Design  │  Build  │  Test   │ Release │  Deploy │
│ Operate  │ Retire  │                                        │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   Integration Layer                          │
│  (Security Tools, Cloud Providers, AI Services, Databases)  │
└─────────────────────────────────────────────────────────────┘
```

## Component Architecture

### Agent Structure

Each agent follows a consistent structure:

```python
class Agent:
    """Base agent structure."""
    
    def __init__(self, config: Config):
        self.config = config
        self.llm_client = self._init_llm()
        self.integrations = self._init_integrations()
    
    def analyze(self, input_data: Input) -> Output:
        """Main analysis method."""
        # 1. Validate input
        validated = self._validate_input(input_data)
        
        # 2. Collect context
        context = self._gather_context(validated)
        
        # 3. AI analysis
        analysis = self._ai_analyze(context)
        
        # 4. Enrich results
        enriched = self._enrich_results(analysis)
        
        # 5. Return structured output
        return self._format_output(enriched)
```

### Data Flow

```
Input → Validation → Context Gathering → AI Analysis → 
Enrichment → Integration → Output → Storage
```

## Phase Architecture

### 1. Plan Phase

```
User Stories/Epics
       ↓
Roadmapping Agent → Security Requirements
       ↓
Policy Scout → Compliance Frameworks
       ↓
Output: Security Requirements + Standards
```

### 2. Design Phase

```
Architecture Diagrams
       ↓
Design Reviewer → Threat Model (STRIDE)
       ↓
Cloud/IaC Architect → Reference Architecture
       ↓
Abuse Case Writer → Attack Scenarios
       ↓
Output: Threats + Mitigations + Test Cases
```

### 3. Build Phase

```
Source Code + Dependencies
       ↓
Code Reviewer → SAST Findings
       ↓
Supply Chain Sentinel → SCA Findings + SBOM
       ↓
IaC Linter → Infrastructure Issues
       ↓
Output: Consolidated Build-Time Findings
```

### 4. Test Phase

```
Running Application
       ↓
DAST/API Fuzzer → Runtime Vulnerabilities
       ↓
Runtime Posture Check → Config Issues
       ↓
Finding Correlator → Deduplicated Findings
       ↓
Output: Prioritized Vulnerability List
```

### 5. Release Phase

```
Release Candidate + Findings
       ↓
Release Gatekeeper → Policy Evaluation
       ↓
Risk Notary → Risk Assessment
       ↓
Output: Release Decision + Documentation
```

### 6. Deploy Phase

```
Deployment Artifacts
       ↓
Deploy Guardian → Security Config Validation
       ↓
Provenance Verifier → Integrity Verification
       ↓
Ops Handoff Coach → Operational Docs
       ↓
Output: Validated Deployment + Runbooks
```

### 7. Operate Phase

```
Production Telemetry
       ↓
Detection Analyst → Security Incidents
       ↓
Vuln Intake Router → Triaged Vulnerabilities
       ↓
Drift Watcher → Configuration Drift
       ↓
Output: Operational Insights → Feedback to Plan
```

### 8. Retire Phase

```
EOL Services/Components
       ↓
Decom Planner → Decommission Checklist
       ↓
Data Steward → Data Retention Plan
       ↓
Legacy Watch → EOL Monitoring
       ↓
Output: Safe Retirement Plan
```

## Integration Patterns

### 1. CI/CD Integration

```yaml
# GitHub Actions Example
- name: DevSecOps Security Scan
  uses: devsecops-ai/scan-action@v1
  with:
    phase: build
    agents: code-reviewer,supply-chain-sentinel
    fail-on: critical,high
```

### 2. API Integration

```python
# REST API
POST /api/v1/agents/build/code-reviewer/analyze
{
  "repository": "owner/repo",
  "pr_number": 42,
  "config": {
    "severity_threshold": "medium"
  }
}
```

### 3. Event-Driven Integration

```python
# Webhook/Event Handler
@event_handler("pull_request.opened")
def on_pr_opened(event):
    agent = CodeReviewer()
    results = agent.analyze(event.pr)
    post_comment(event.pr, results.summary)
```

## AI/LLM Integration

### Prompt Engineering

Agents use carefully crafted prompts for different tasks:

```python
THREAT_MODELING_PROMPT = """
Analyze this architecture for security threats using STRIDE:
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

Architecture: {architecture}
Components: {components}

Provide specific threats for each component and suggest mitigations.
"""
```

### Model Selection

- **GPT-4** - Complex reasoning, threat modeling
- **Claude** - Code review, documentation generation
- **Specialized Models** - Code-specific tasks (CodeLLAMA, StarCoder)

## Data Models

### Common Models

```python
class Finding(BaseModel):
    """Security finding model."""
    id: str
    severity: Severity
    title: str
    description: str
    location: Location
    cwe_id: Optional[str]
    cvss_score: Optional[float]
    remediation: str
    references: List[str]

class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

class Location(BaseModel):
    file_path: str
    line_start: int
    line_end: Optional[int]
    code_snippet: Optional[str]
```

## Scalability Considerations

### 1. **Horizontal Scaling**
- Agents can run independently
- Queue-based task distribution
- Stateless design

### 2. **Caching**
- Cache AI model responses
- Cache security scan results
- Cache policy lookups

### 3. **Async Operations**
```python
async def analyze_repository(repo):
    async with asyncio.TaskGroup() as tg:
        sast = tg.create_task(code_reviewer.analyze())
        sca = tg.create_task(supply_chain.analyze())
        iac = tg.create_task(iac_linter.analyze())
    
    return correlate([sast.result(), sca.result(), iac.result()])
```

## Security Considerations

### 1. **Secrets Management**
- Never log secrets
- Use secure secret storage (Vault, AWS Secrets Manager)
- Rotate API keys regularly

### 2. **Access Control**
- Role-based access control (RBAC)
- Principle of least privilege
- Audit logging

### 3. **Data Privacy**
- Anonymize sensitive data before AI processing
- Comply with data residency requirements
- Implement data retention policies

## Extensibility

### Adding Custom Agents

```python
from shared.base_agent import BaseAgent

class CustomAgent(BaseAgent):
    """Custom security agent."""
    
    def analyze(self, input_data):
        # Custom logic
        return results
```

### Custom Integrations

```python
from shared.integrations import BaseIntegration

class CustomToolIntegration(BaseIntegration):
    """Integration with custom security tool."""
    
    def scan(self, target):
        # Integration logic
        return findings
```

## Monitoring & Observability

### Metrics

- Agent execution time
- Finding counts by severity
- False positive rates
- Integration success rates

### Logging

```python
logger.info("Agent executed", extra={
    "agent": "code_reviewer",
    "duration_ms": 1234,
    "findings": 5,
    "severity_breakdown": {"high": 2, "medium": 3}
})
```

### Tracing

Distributed tracing for pipeline visibility:
- OpenTelemetry integration
- Span tracking across agents
- Performance bottleneck identification

## Future Architecture Enhancements

1. **Multi-tenant Support** - Isolated environments for different teams
2. **Real-time Collaboration** - Live agent feedback in development
3. **ML Model Training** - Custom models trained on organizational data
4. **Graph-based Analysis** - Relationship mapping between findings
5. **Autonomous Remediation** - Auto-fix capabilities with human approval

