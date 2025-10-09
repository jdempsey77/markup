# Release Phase Agents

## Overview
The Release phase agents enforce security gates and document release risks.

## Agents

### 1. Release Gatekeeper
**Purpose**: Enforces policy-as-code and manages security exceptions for releases.

**Capabilities**:
- Policy-as-code enforcement
- Release gate validation
- Exception workflow management
- Security threshold enforcement
- Approval automation

**Integration Points**:
- CI/CD pipelines
- Policy engines (OPA, Kyverno)
- Release management tools

### 2. Risk Notary
**Purpose**: Generates risk memos and evidence packages for releases.

**Capabilities**:
- Automated risk assessment
- Evidence collection and packaging
- Risk memo generation
- Compliance documentation
- Audit trail creation

**Integration Points**:
- GRC platforms
- Document management systems
- Audit logging systems

## Usage

```python
from phases.release.release_gatekeeper import ReleaseGatekeeper
from phases.release.risk_notary import RiskNotary

# Gate Enforcement
gatekeeper = ReleaseGatekeeper()
gate_result = gatekeeper.evaluate_release(
    release_id="v1.2.3",
    findings=all_findings
)

# Risk Documentation
notary = RiskNotary()
risk_memo = notary.generate_risk_memo(
    release_id="v1.2.3",
    findings=all_findings,
    mitigations=applied_mitigations
)
```

## Configuration

See `config/release.yaml` for configuration options.

