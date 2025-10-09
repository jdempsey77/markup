"""
Setup configuration for DevSecOps AI Agent Framework
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="devsecops-ai-agents",
    version="0.1.0",
    description="AI-powered security agent framework spanning the entire SDLC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DevSecOps Community",
    author_email="security@example.com",
    url="https://github.com/jdempsey77/markup",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*", "examples", "docs"]),
    install_requires=[
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
        "openai>=1.0.0",
        "anthropic>=0.7.0",
        "langchain>=0.1.0",
        "bandit>=1.7.5",
        "safety>=2.3.5",
        "semgrep>=1.45.0",
        "boto3>=1.28.0",
        "fastapi>=0.104.1",
        "sqlalchemy>=2.0.23",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0",
            "pre-commit>=3.5.0",
        ],
        "docs": [
            "mkdocs>=1.5.3",
            "mkdocs-material>=9.4.14",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
    ],
    keywords="security devsecops ai agents sdlc appsec",
    entry_points={
        "console_scripts": [
            "devsecops-agent=cli:main",
        ],
    },
)

