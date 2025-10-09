# Configuration Reference

## Overview

The DevSecOps AI Agent Framework uses YAML-based configuration files for customizing agent behavior, integrations, and policies.

## Configuration Hierarchy

```
1. Default Configuration (built-in)
2. Global Configuration (config/global.yaml)
3. Phase Configuration (config/{phase}.yaml)
4. Agent Configuration (config/agents/{agent}.yaml)
5. Environment Variables (.env)
6. Runtime Parameters (API/CLI)
```

Later configurations override earlier ones.

## Global Configuration

### config/global.yaml

```yaml
# Global Framework Configuration

# AI/LLM Provider Settings
ai:
  default_provider: openai
  providers:
    openai:
      model: gpt-4-turbo-preview
      api_key: ${OPENAI_API_KEY}
      max_tokens: 4000
      temperature: 0.1
    anthropic:
      model: claude-3-opus-20240229
      api_key: ${ANTHROPIC_API_KEY}
      max_tokens: 4000
      temperature: 0.1
  
  # Retry and timeout settings
  retry:
    max_attempts: 3
    backoff_multiplier: 2
    max_backoff_seconds: 60
  timeout_seconds: 300

# Logging Configuration
logging:
  level: INFO
  format: json
  outputs:
    - type: console
    - type: file
      path: logs/framework.log
      rotation: daily
      retention_days: 30
  
  # Log specific events
  events:
    agent_execution: true
    finding_detected: true
    integration_calls: true
    errors: true

# Database Configuration
database:
  url: ${DATABASE_URL}
  pool_size: 10
  max_overflow: 20
  echo: false

# Caching Configuration
cache:
  enabled: true
  backend: redis
  url: ${REDIS_URL}
  ttl_seconds: 3600
  
  # What to cache
  cache_items:
    ai_responses: true
    scan_results: true
    policy_lookups: true

# Security Settings
security:
  # Secret scanning
  secret_detection:
    enabled: true
    patterns_file: config/secret-patterns.yaml
  
  # Data anonymization before AI processing
  anonymize_data: true
  anonymize_patterns:
    - email
    - ip_address
    - api_key
    - password

# Integration Settings
integrations:
  github:
    api_url: https://api.github.com
    token: ${GITHUB_TOKEN}
    org: ${GITHUB_ORG}
  
  jira:
    url: ${JIRA_URL}
    username: ${JIRA_USERNAME}
    api_token: ${JIRA_API_TOKEN}
  
  slack:
    webhook_url: ${SLACK_WEBHOOK_URL}
    channel: #security-alerts

# Notification Settings
notifications:
  enabled: true
  channels:
    - slack
    - email
  
  # When to notify
  triggers:
    critical_finding: true
    release_gate_failed: true
    deployment_issue: true
  
  email:
    smtp_host: ${EMAIL_SMTP_HOST}
    smtp_port: ${EMAIL_SMTP_PORT}
    from: ${EMAIL_FROM}
    to:
      - security@example.com

# Phase Enablement
phases:
  plan: true
  design: true
  build: true
  test: true
  release: true
  deploy: true
  operate: true
  retire: true
```

## Phase-Specific Configuration

### config/build.yaml

```yaml
# Build Phase Configuration

phase: build

# Agent enablement
agents:
  code_reviewer:
    enabled: true
    config:
      # SAST Tools
      sast_tools:
        - semgrep
        - bandit
        - eslint
      
      # Severity threshold
      fail_on_severity:
        - critical
        - high
      
      # PR comment settings
      post_comments: true
      comment_style: grouped  # grouped | inline
      
      # Rules
      rule_sets:
        - owasp-top-10
        - cwe-top-25
        - custom-rules
  
  supply_chain_sentinel:
    enabled: true
    config:
      # SCA Tools
      sca_tools:
        - snyk
        - dependabot
        - trivy
      
      # License checking
      allowed_licenses:
        - MIT
        - Apache-2.0
        - BSD-3-Clause
      
      blocked_licenses:
        - GPL-3.0
        - AGPL-3.0
      
      # SBOM generation
      sbom:
        enabled: true
        format: cyclonedx  # cyclonedx | spdx
        include_dev_deps: false
      
      # Vulnerability thresholds
      vulnerability_policy:
        max_critical: 0
        max_high: 5
        max_medium: 20
  
  iac_linter:
    enabled: true
    config:
      # IaC Tools
      tools:
        - checkov
        - tfsec
        - trivy
      
      # Frameworks to scan
      frameworks:
        - terraform
        - cloudformation
        - kubernetes
        - docker
      
      # Cloud providers
      cloud_providers:
        - aws
        - azure
        - gcp
      
      # Policies
      policies:
        - cis-benchmarks
        - nist-800-53
        - custom-policies

# Execution Settings
execution:
  parallel: true
  max_concurrent_agents: 3
  timeout_minutes: 30
  
  # Failure handling
  on_failure:
    action: notify  # notify | fail | ignore
    retry: true
    max_retries: 2
```

### config/test.yaml

```yaml
# Test Phase Configuration

phase: test

agents:
  dast_api_fuzzer:
    enabled: true
    config:
      # DAST Tools
      tools:
        - owasp-zap
        - burp-suite
      
      # Target configuration
      target:
        base_url: ${TEST_TARGET_URL}
        auth:
          type: oauth2  # oauth2 | basic | bearer | api_key
          credentials: ${TEST_AUTH_CREDENTIALS}
      
      # API specification
      api_spec:
        format: openapi  # openapi | graphql | grpc
        file: api/openapi.yaml
      
      # Scan configuration
      scan:
        depth: medium  # light | medium | deep
        max_duration_minutes: 60
        
        # OWASP Top 10 tests
        tests:
          - sql_injection
          - xss
          - broken_auth
          - sensitive_data_exposure
          - xxe
          - broken_access_control
          - security_misconfiguration
          - csrf
          - insecure_deserialization
          - vulnerable_components
      
      # Headers to test
      security_headers:
        - Content-Security-Policy
        - X-Frame-Options
        - X-Content-Type-Options
        - Strict-Transport-Security
  
  runtime_posture_check:
    enabled: true
    config:
      # Container scanning
      container:
        registry: ${CONTAINER_REGISTRY}
        image: ${IMAGE_NAME}:${IMAGE_TAG}
        
        # Scan for
        scan_for:
          - vulnerabilities
          - secrets
          - misconfigurations
          - malware
      
      # Benchmark compliance
      benchmarks:
        - cis-docker
        - cis-kubernetes
      
      # Configuration checks
      configs:
        - dockerfile_best_practices
        - kubernetes_security_context
        - network_policies
  
  finding_correlator:
    enabled: true
    config:
      # Deduplication
      dedup:
        enabled: true
        match_threshold: 0.85
        merge_similar: true
      
      # Enrichment
      enrichment:
        - add_cwe_info
        - add_cvss_score
        - add_exploit_availability
        - add_fix_guidance
      
      # Prioritization
      prioritization:
        algorithm: risk_based  # risk_based | cvss | custom
        factors:
          - severity
          - exploitability
          - asset_criticality
          - data_sensitivity
      
      # Grouping
      grouping:
        by:
          - component
          - vulnerability_type
          - severity

# Output Configuration
output:
  formats:
    - sarif
    - json
    - html
  
  destinations:
    - github_security
    - jira
    - local_file
```

## Agent-Specific Configuration

### config/agents/code-reviewer.yaml

```yaml
# Code Reviewer Agent Configuration

agent: code_reviewer
phase: build

# Language-specific settings
languages:
  python:
    tools:
      - bandit
      - semgrep
    rules:
      - hardcoded-credentials
      - sql-injection
      - command-injection
    
  javascript:
    tools:
      - eslint-security
      - semgrep
    rules:
      - xss
      - prototype-pollution
      - unsafe-regex
  
  java:
    tools:
      - spotbugs
      - semgrep
    rules:
      - xxe
      - deserialization
      - weak-crypto

# AI-powered review
ai_review:
  enabled: true
  model: gpt-4
  
  # What to analyze
  analyze:
    - security_patterns
    - code_smells
    - best_practices
    - performance_issues
  
  # Prompt configuration
  prompts:
    system_prompt: |
      You are a security expert reviewing code for vulnerabilities.
      Focus on OWASP Top 10 and CWE Top 25 issues.
      Provide specific, actionable recommendations.
    
    code_review_prompt: |
      Review this code change for security issues:
      {code_diff}
      
      Identify:
      1. Security vulnerabilities
      2. Insecure coding patterns
      3. Potential data leaks
      4. Authentication/authorization issues
      
      For each issue, provide:
      - Severity (critical/high/medium/low)
      - Description
      - Remediation steps
      - Code example of fix

# Secret detection
secrets:
  enabled: true
  patterns:
    - aws_access_key
    - github_token
    - private_key
    - password
    - api_key
  
  # Entropy analysis
  entropy_check:
    enabled: true
    threshold: 4.5
  
  # Allowlist
  allowlist_file: .secret-allowlist

# PR commenting
pull_request:
  auto_comment: true
  
  # Comment template
  comment_template: |
    ## 🔒 Security Review
    
    Found **{finding_count}** security issues:
    
    ### Critical: {critical_count}
    ### High: {high_count}
    ### Medium: {medium_count}
    ### Low: {low_count}
    
    {detailed_findings}
    
    ---
    *Powered by DevSecOps AI Agent Framework*
  
  # When to comment
  comment_on:
    - findings_detected
    - no_issues_found
  
  # Auto-approve
  auto_approve:
    enabled: false
    conditions:
      - no_critical
      - no_high
      - code_coverage_increased
```

## Environment Variables

### .env

```bash
# AI Providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
AZURE_OPENAI_ENDPOINT=https://...
AZURE_OPENAI_KEY=...

# GitHub
GITHUB_TOKEN=ghp_...
GITHUB_ORG=my-org

# Security Tools
SONARQUBE_URL=https://sonarqube.example.com
SONARQUBE_TOKEN=squ_...
SNYK_TOKEN=...
SEMGREP_TOKEN=...

# Cloud Providers
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=us-east-1

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/devsecops
REDIS_URL=redis://localhost:6379/0

# Notifications
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
EMAIL_SMTP_HOST=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_FROM=security@example.com

# Feature Flags
ENABLE_AI_REVIEW=true
ENABLE_AUTO_FIX=false
ENABLE_TELEMETRY=true
```

## Runtime Configuration

### CLI Arguments

```bash
# Override phase
devsecops-agent --phase build --agent code-reviewer

# Override config
devsecops-agent --config custom-config.yaml

# Set log level
devsecops-agent --log-level debug

# Specify output format
devsecops-agent --output-format sarif --output-file results.sarif
```

### API Configuration

```python
from devsecops_framework import Pipeline

pipeline = Pipeline(
    config_path="custom-config.yaml",
    overrides={
        "ai.provider": "anthropic",
        "logging.level": "DEBUG",
        "phases.build.agents.code_reviewer.enabled": True
    }
)

results = pipeline.run(phase="build")
```

## Best Practices

1. **Never commit secrets** - Use environment variables
2. **Use config inheritance** - Extend base configurations
3. **Version control configs** - Track configuration changes
4. **Document custom settings** - Add comments for clarity
5. **Validate configurations** - Use schema validation
6. **Separate environments** - Different configs for dev/staging/prod

## Configuration Validation

```bash
# Validate configuration
devsecops-agent validate-config --file config/build.yaml

# Test configuration
devsecops-agent test-config --phase build --dry-run
```

## Troubleshooting

### Common Issues

1. **API key errors** - Check environment variables are set
2. **Tool not found** - Ensure tools are installed and in PATH
3. **Permission denied** - Check file/directory permissions
4. **Timeout errors** - Increase timeout values in config
5. **Memory issues** - Reduce parallel execution or increase limits

