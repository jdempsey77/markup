# Operate/Monitor Phase Agents

## Overview
The Operate/Monitor phase agents provide continuous security monitoring and incident response.

## Agents

### 1. Detection Analyst
**Purpose**: Converts security signals into actionable hypotheses.

**Capabilities**:
- Security event analysis
- Anomaly detection
- Threat hypothesis generation
- Alert correlation
- False positive reduction

**Integration Points**:
- SIEM systems (Splunk, Elastic)
- Security analytics platforms
- Log aggregation systems
- Threat intelligence feeds

### 2. Vuln Intake Router
**Purpose**: Prioritizes and routes vulnerabilities according to SLAs.

**Capabilities**:
- Vulnerability triage and prioritization
- SLA-based routing
- Risk-based prioritization
- Assignment automation
- Escalation management

**Integration Points**:
- Vulnerability scanners
- Ticketing systems (Jira, ServiceNow)
- Asset management
- CMDB

### 3. Drift Watcher
**Purpose**: Monitors configuration and security posture variance.

**Capabilities**:
- Configuration drift detection
- Baseline comparison
- Compliance monitoring
- Unauthorized change detection
- Posture degradation alerts

**Integration Points**:
- Cloud security posture management (CSPM)
- Infrastructure monitoring
- Configuration management databases
- Version control systems

## Usage

```python
from phases.operate.detection_analyst import DetectionAnalyst
from phases.operate.vuln_intake_router import VulnIntakeRouter
from phases.operate.drift_watcher import DriftWatcher

# Detection Analysis
analyst = DetectionAnalyst()
incidents = analyst.analyze_signals(
    time_range="last_1h",
    signal_sources=["waf", "ids", "auth_logs"]
)

# Vulnerability Routing
router = VulnIntakeRouter()
assignments = router.route_vulnerabilities(
    vulnerabilities=new_vulns,
    sla_config=sla_rules
)

# Drift Monitoring
watcher = DriftWatcher()
drift_report = watcher.check_drift(
    baseline="approved_config.yaml",
    current_state="live_config.yaml"
)
```

## Configuration

See `config/operate.yaml` for configuration options.

