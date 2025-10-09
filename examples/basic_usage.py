"""
Basic Usage Examples for DevSecOps AI Agent Framework
"""

# Example 1: Run a single agent
def example_roadmapping_agent():
    """Example: Use Roadmapping Agent to analyze an epic."""
    from phases.plan.roadmapping_agent import RoadmappingAgent
    
    agent = RoadmappingAgent()
    
    result = agent.analyze_epic(
        epic_id="EPIC-123",
        description="Build a user authentication system with OAuth2 and MFA support",
        project_type="web_app"
    )
    
    print("=== Security Requirements ===")
    for req in result['security_requirements']:
        print(f"- [{req.priority.upper()}] {req.title}")
        print(f"  {req.description}")
    
    print("\n=== Risk Hints ===")
    for risk in result['risk_hints']:
        print(f"- [{risk.severity.upper()}] {risk.risk_type}")
        print(f"  {risk.description}")
    
    print("\n=== Recommendations ===")
    for rec in result['recommendations']:
        print(f"- {rec}")


# Example 2: Find compliance standards
def example_policy_scout():
    """Example: Use Policy Scout to find applicable standards."""
    from phases.plan.policy_scout import PolicyScout
    
    scout = PolicyScout()
    
    standards = scout.find_standards(
        industry="fintech",
        data_types=["PII", "payment_card_data"],
        regions=["US", "EU"]
    )
    
    print("=== Applicable Standards ===")
    for standard in standards:
        print(f"\n{standard.framework} v{standard.version}")
        print(f"Priority: {standard.priority}")
        print(f"Reason: {standard.applicable_reason}")
        print(f"Key Controls: {', '.join(standard.controls[:3])}")
    
    # Get baseline policies
    policies = scout.get_baseline_policies(standards)
    
    print("\n=== Baseline Security Policies ===")
    for category, requirements in policies.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for req in requirements:
            print(f"  - {req}")


# Example 3: Run complete pipeline for a phase
def example_pipeline_single_phase():
    """Example: Run complete Plan phase."""
    from pipeline import DevSecOpsPipeline, Phase
    
    pipeline = DevSecOpsPipeline()
    
    results = pipeline.run_phase(
        Phase.PLAN,
        epic_id="EPIC-456",
        description="Build healthcare patient portal with HIPAA compliance",
        project_type="web_app",
        industry="healthcare",
        data_types=["PHI", "PII"],
        regions=["US"]
    )
    
    print("=== Plan Phase Results ===")
    if "roadmapping" in results:
        print(f"\nSecurity Requirements: {len(results['roadmapping']['security_requirements'])}")
        print(f"Risk Hints: {len(results['roadmapping']['risk_hints'])}")
    
    if "policy" in results:
        print(f"\nApplicable Standards: {len(results['policy'])}")


# Example 4: Run full pipeline
def example_full_pipeline():
    """Example: Run complete security pipeline."""
    from pipeline import DevSecOpsPipeline
    
    pipeline = DevSecOpsPipeline(config_path="config/global.yaml")
    
    results = pipeline.run_all_phases(
        project="payment-api",
        branch="feature/new-payment-method",
        epic_id="EPIC-789",
        description="Add cryptocurrency payment support",
        industry="fintech"
    )
    
    print("=== Full Pipeline Results ===")
    for phase, phase_results in results.items():
        print(f"\n{phase.upper()} Phase:")
        if isinstance(phase_results, dict) and "error" in phase_results:
            print(f"  Error: {phase_results['error']}")
        else:
            print(f"  Status: Completed")


# Example 5: Custom agent configuration
def example_custom_config():
    """Example: Use custom configuration."""
    from phases.plan.roadmapping_agent import RoadmappingAgent
    
    # With custom config file
    agent = RoadmappingAgent(config_path="config/agents/custom-roadmap.yaml")
    
    result = agent.analyze_epic(
        epic_id="EPIC-999",
        description="Implement API rate limiting and DDoS protection"
    )
    
    print(f"Found {len(result['security_requirements'])} requirements")


# Example 6: Working with findings
def example_findings_processing():
    """Example: Process security findings."""
    from phases.plan.roadmapping_agent import RoadmappingAgent
    
    agent = RoadmappingAgent()
    result = agent.analyze_epic(
        epic_id="EPIC-111",
        description="Build admin dashboard with role-based access control"
    )
    
    # Filter high priority requirements
    high_priority = [
        req for req in result['security_requirements']
        if req.priority in ['critical', 'high']
    ]
    
    print(f"=== High Priority Requirements ({len(high_priority)}) ===")
    for req in high_priority:
        print(f"\n{req.title}")
        print(f"Category: {req.category}")
        print(f"Compliance: {', '.join(req.compliance_mappings)}")
        print(f"Description: {req.description}")


if __name__ == "__main__":
    print("DevSecOps AI Agent Framework - Examples\n")
    
    print("\n" + "="*60)
    print("Example 1: Roadmapping Agent")
    print("="*60)
    example_roadmapping_agent()
    
    print("\n" + "="*60)
    print("Example 2: Policy Scout")
    print("="*60)
    example_policy_scout()
    
    print("\n" + "="*60)
    print("Example 3: Single Phase Pipeline")
    print("="*60)
    example_pipeline_single_phase()
    
    # Uncomment to run other examples
    # example_full_pipeline()
    # example_custom_config()
    # example_findings_processing()

