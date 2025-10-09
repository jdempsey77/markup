# Deploy Phase Agents

## Overview
The Deploy phase agents ensure secure deployment and proper operational handoff.

## Agents

### 1. Deploy Guardian
**Purpose**: Validates WAAP/WAF rules and secrets management during deployment.

**Capabilities**:
- WAF/WAAP rule validation
- Secrets management verification
- Deployment security checks
- Configuration validation
- Production readiness assessment

**Integration Points**:
- AWS WAF, Cloudflare, Azure WAF
- HashiCorp Vault, AWS Secrets Manager
- Kubernetes Secrets
- Deployment tools (Kubernetes, Helm)

### 2. Provenance Verifier
**Purpose**: Verifies code signing and SBOM attestation.

**Capabilities**:
- Code signing verification
- SBOM attestation validation
- Supply chain integrity checks
- Artifact provenance tracking
- Build reproducibility verification

**Integration Points**:
- Sigstore, cosign
- In-toto, SLSA
- Container registries
- Artifact repositories

### 3. Ops Handoff Coach
**Purpose**: Creates playbooks and monitoring configurations for operations team.

**Capabilities**:
- Runbook generation
- Monitoring setup automation
- Alert configuration
- Incident response playbooks
- Operational documentation

**Integration Points**:
- Prometheus, Grafana
- PagerDuty, OpsGenie
- Documentation platforms
- Monitoring systems

## Usage

```python
from phases.deploy.deploy_guardian import DeployGuardian
from phases.deploy.provenance_verifier import ProvenanceVerifier
from phases.deploy.ops_handoff_coach import OpsHandoffCoach

# Deployment Security
guardian = DeployGuardian()
deploy_checks = guardian.validate_deployment(
    environment="production",
    manifest="k8s-manifest.yaml"
)

# Provenance Verification
verifier = ProvenanceVerifier()
is_valid = verifier.verify_artifact(
    artifact="myapp:v1.2.3",
    sbom="sbom.json"
)

# Operations Handoff
coach = OpsHandoffCoach()
playbook = coach.generate_runbook(
    service="payment-api",
    deployment_info=deploy_info
)
```

## Configuration

See `config/deploy.yaml` for configuration options.

