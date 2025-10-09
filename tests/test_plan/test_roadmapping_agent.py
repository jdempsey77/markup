"""
Tests for Roadmapping Agent
"""

import pytest
from phases.plan.roadmapping_agent import RoadmappingAgent, SecurityRequirement, RiskHint


class TestRoadmappingAgent:
    """Test suite for Roadmapping Agent."""
    
    def test_agent_initialization(self):
        """Test agent can be initialized."""
        agent = RoadmappingAgent()
        assert agent is not None
        assert agent.config is not None
    
    def test_analyze_epic_basic(self):
        """Test basic epic analysis."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-001",
            description="Build user authentication system"
        )
        
        assert result is not None
        assert "epic_id" in result
        assert result["epic_id"] == "TEST-001"
        assert "security_requirements" in result
        assert "risk_hints" in result
        assert "recommendations" in result
    
    def test_identifies_authentication_requirements(self):
        """Test agent identifies authentication requirements."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-002",
            description="Add user login and registration features"
        )
        
        auth_reqs = [
            req for req in result['security_requirements']
            if 'authentication' in req.category.lower()
        ]
        
        assert len(auth_reqs) > 0
    
    def test_identifies_payment_requirements(self):
        """Test agent identifies payment security requirements."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-003",
            description="Implement payment processing with credit cards"
        )
        
        payment_reqs = [
            req for req in result['security_requirements']
            if 'payment' in req.description.lower() or 'pci' in ' '.join(req.compliance_mappings).lower()
        ]
        
        assert len(payment_reqs) > 0
    
    def test_identifies_api_risks(self):
        """Test agent identifies API security risks."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-004",
            description="Create REST API for mobile app"
        )
        
        api_risks = [
            risk for risk in result['risk_hints']
            if 'api' in risk.risk_type.lower()
        ]
        
        assert len(api_risks) > 0
    
    def test_handles_empty_description(self):
        """Test agent handles empty description gracefully."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-005",
            description=""
        )
        
        assert result is not None
        assert "security_requirements" in result
        assert isinstance(result["security_requirements"], list)
    
    def test_security_requirement_model(self):
        """Test SecurityRequirement model."""
        req = SecurityRequirement(
            id="SEC-001",
            title="Test Requirement",
            description="Test description",
            priority="high",
            category="authentication",
            compliance_mappings=["OWASP"]
        )
        
        assert req.id == "SEC-001"
        assert req.priority == "high"
        assert "OWASP" in req.compliance_mappings
    
    def test_risk_hint_model(self):
        """Test RiskHint model."""
        risk = RiskHint(
            risk_type="Injection",
            severity="high",
            description="SQL injection risk",
            mitigation_suggestions=["Use parameterized queries"]
        )
        
        assert risk.risk_type == "Injection"
        assert risk.severity == "high"
        assert len(risk.mitigation_suggestions) > 0
    
    def test_generates_recommendations(self):
        """Test agent generates recommendations."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-006",
            description="Build admin dashboard with user management"
        )
        
        assert "recommendations" in result
        assert isinstance(result["recommendations"], list)
    
    def test_project_type_consideration(self):
        """Test agent considers project type."""
        agent = RoadmappingAgent()
        
        result = agent.analyze_epic(
            epic_id="TEST-007",
            description="Create new feature",
            project_type="api"
        )
        
        assert result is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

