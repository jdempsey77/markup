# Test Phase Agents

## Overview
The Test phase agents perform dynamic security testing and vulnerability analysis.

## Agents

### 1. DAST/API Fuzzer
**Purpose**: Dynamic application security testing focused on auth flows, headers, and OWASP Top 10.

**Capabilities**:
- Dynamic application security testing (DAST)
- API fuzzing and testing
- Authentication flow testing
- HTTP header security analysis
- OWASP Top 10 vulnerability detection

**Integration Points**:
- OWASP ZAP, Burp Suite
- Postman, REST-assured
- API specifications (OpenAPI/Swagger)

### 2. Runtime Posture Check
**Purpose**: Validates container images, configurations, and detects runtime drift.

**Capabilities**:
- Container image vulnerability scanning
- Runtime configuration validation
- Security posture assessment
- Configuration drift detection
- Compliance verification

**Integration Points**:
- Docker, Kubernetes
- Container registries
- Runtime security tools (Falco, Aqua)

### 3. Finding Correlator
**Purpose**: De-duplicates, enriches, and groups security findings.

**Capabilities**:
- Cross-tool finding correlation
- Vulnerability deduplication
- Risk scoring and prioritization
- Finding enrichment with context
- Grouped reporting

**Integration Points**:
- SAST, DAST, SCA tools
- Vulnerability databases (NVD, CVE)
- Security orchestration platforms

## Usage

```python
from phases.test.dast_api_fuzzer import DASTAPIFuzzer
from phases.test.runtime_posture_check import RuntimePostureCheck
from phases.test.finding_correlator import FindingCorrelator

# DAST Testing
fuzzer = DASTAPIFuzzer()
vulnerabilities = fuzzer.test_api(
    api_url="https://api.example.com",
    spec_file="openapi.yaml"
)

# Runtime Checks
posture_check = RuntimePostureCheck()
issues = posture_check.scan_container(
    image="myapp:latest"
)

# Correlate Findings
correlator = FindingCorrelator()
deduplicated = correlator.correlate_findings([
    sast_findings,
    dast_findings,
    sca_findings
])
```

## Configuration

See `config/test.yaml` for configuration options.

