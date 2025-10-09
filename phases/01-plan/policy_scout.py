"""
Policy Scout Agent - Looks up compliance baselines and security standards.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel
from enum import Enum


class ComplianceFramework(str, Enum):
    """Common compliance frameworks."""
    ISO_27001 = "ISO 27001"
    SOC2 = "SOC 2"
    NIST_CSF = "NIST Cybersecurity Framework"
    PCI_DSS = "PCI-DSS"
    HIPAA = "HIPAA"
    GDPR = "GDPR"
    CCPA = "CCPA"
    OWASP_ASVS = "OWASP ASVS"
    CIS_CONTROLS = "CIS Controls"


class SecurityStandard(BaseModel):
    """Security standard model."""
    framework: str
    version: str
    controls: List[str]
    applicable_reason: str
    priority: str


class PolicyScout:
    """
    Policy Scout identifies relevant compliance frameworks and
    security standards based on project characteristics.
    """
    
    def __init__(self):
        """Initialize Policy Scout."""
        self.framework_mappings = self._load_framework_mappings()
    
    def _load_framework_mappings(self) -> Dict:
        """Load framework mappings and requirements."""
        return {
            "fintech": [
                ComplianceFramework.PCI_DSS,
                ComplianceFramework.SOC2,
                ComplianceFramework.ISO_27001
            ],
            "healthcare": [
                ComplianceFramework.HIPAA,
                ComplianceFramework.SOC2,
                ComplianceFramework.ISO_27001
            ],
            "saas": [
                ComplianceFramework.SOC2,
                ComplianceFramework.ISO_27001,
                ComplianceFramework.GDPR
            ],
            "ecommerce": [
                ComplianceFramework.PCI_DSS,
                ComplianceFramework.GDPR,
                ComplianceFramework.CCPA
            ]
        }
    
    def find_standards(
        self,
        industry: str,
        data_types: Optional[List[str]] = None,
        regions: Optional[List[str]] = None
    ) -> List[SecurityStandard]:
        """
        Find applicable security standards and compliance frameworks.
        
        Args:
            industry: Industry sector (fintech, healthcare, saas, etc.)
            data_types: Types of data being processed (PII, PHI, payment_card_data)
            regions: Geographic regions (EU, US, APAC, etc.)
            
        Returns:
            List of applicable security standards
        """
        standards = []
        data_types = data_types or []
        regions = regions or []
        
        # Industry-specific frameworks
        if industry in self.framework_mappings:
            for framework in self.framework_mappings[industry]:
                standards.append(self._get_framework_details(framework, industry))
        
        # Data-type specific requirements
        if "PII" in data_types or "personal_data" in data_types:
            if "EU" in regions:
                standards.append(SecurityStandard(
                    framework=ComplianceFramework.GDPR,
                    version="2016/679",
                    controls=["Art. 32 - Security of processing", "Art. 25 - Data protection by design"],
                    applicable_reason="Processing personal data of EU residents",
                    priority="high"
                ))
        
        if "payment_card_data" in data_types:
            standards.append(SecurityStandard(
                framework=ComplianceFramework.PCI_DSS,
                version="4.0",
                controls=["Requirement 3", "Requirement 4", "Requirement 8"],
                applicable_reason="Processing payment card information",
                priority="critical"
            ))
        
        # Always include OWASP for web applications
        standards.append(SecurityStandard(
            framework=ComplianceFramework.OWASP_ASVS,
            version="4.0",
            controls=["V1: Architecture", "V2: Authentication", "V3: Session Management"],
            applicable_reason="Web application security baseline",
            priority="high"
        ))
        
        return standards
    
    def _get_framework_details(self, framework: ComplianceFramework, context: str) -> SecurityStandard:
        """Get detailed information about a framework."""
        framework_details = {
            ComplianceFramework.SOC2: SecurityStandard(
                framework=framework.value,
                version="2017",
                controls=["CC6.1", "CC6.6", "CC6.7"],
                applicable_reason=f"Industry standard for {context}",
                priority="high"
            ),
            ComplianceFramework.ISO_27001: SecurityStandard(
                framework=framework.value,
                version="2022",
                controls=["A.5.1", "A.8.1", "A.14.2"],
                applicable_reason="Information security management",
                priority="medium"
            ),
            ComplianceFramework.PCI_DSS: SecurityStandard(
                framework=framework.value,
                version="4.0",
                controls=["Req 1-12"],
                applicable_reason="Payment card data protection",
                priority="critical"
            )
        }
        
        return framework_details.get(framework, SecurityStandard(
            framework=framework.value,
            version="latest",
            controls=[],
            applicable_reason=context,
            priority="medium"
        ))
    
    def get_baseline_policies(self, standards: List[SecurityStandard]) -> Dict[str, List[str]]:
        """
        Get baseline security policies based on applicable standards.
        
        Args:
            standards: List of applicable security standards
            
        Returns:
            Dictionary of policy categories and requirements
        """
        policies = {
            "access_control": [
                "Implement multi-factor authentication for all users",
                "Apply principle of least privilege",
                "Regular access reviews every 90 days"
            ],
            "data_protection": [
                "Encrypt data at rest using AES-256",
                "Encrypt data in transit using TLS 1.2+",
                "Implement data classification scheme"
            ],
            "incident_response": [
                "Maintain incident response plan",
                "Conduct incident response drills quarterly",
                "Define escalation procedures"
            ],
            "logging_monitoring": [
                "Enable comprehensive audit logging",
                "Retain logs for minimum 90 days",
                "Implement real-time alerting for security events"
            ],
            "vulnerability_management": [
                "Scan for vulnerabilities monthly",
                "Patch critical vulnerabilities within 30 days",
                "Maintain asset inventory"
            ]
        }
        
        return policies


if __name__ == "__main__":
    # Example usage
    scout = PolicyScout()
    
    standards = scout.find_standards(
        industry="fintech",
        data_types=["PII", "payment_card_data"],
        regions=["US", "EU"]
    )
    
    print(f"Found {len(standards)} applicable standards:")
    for standard in standards:
        print(f"  - {standard.framework} (Priority: {standard.priority})")
    
    policies = scout.get_baseline_policies(standards)
    print(f"\nBaseline policies across {len(policies)} categories")

