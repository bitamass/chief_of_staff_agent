"""Executable specialist agents used by the Chief of Staff orchestrator."""

from typing import Literal

from agents import Agent
from pydantic import BaseModel, Field

from specialist_skill_loader import load_agent_skills


class NextAction(BaseModel):
    """An action recommended by a specialist agent."""

    action: str
    owner: str
    due_date: str | None = None


class SpecialistResponse(BaseModel):
    """Standard response returned by every specialist agent."""

    assignment_id: str
    agent: Literal[
        "innovation-agent",
        "compliance-agent",
        "project-management-agent",
        "data-analyst-agent",
    ]
    skills_used: list[str] = Field(default_factory=list)
    status: Literal[
        "complete",
        "needs-information",
        "blocked",
        "escalation-required",
    ]
    executive_summary: str
    findings: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    recommendation: str
    decisions_needed: list[str] = Field(default_factory=list)
    next_actions: list[NextAction] = Field(default_factory=list)
    confidence: Literal["high", "medium", "low"]
    limitations: list[str] = Field(default_factory=list)


def build_specialist_instructions(
    agent_id: str,
    role: str,
) -> str:
    """Combine the agent's role with its repository-based skills."""

    skill_instructions = load_agent_skills(agent_id)

    return f"""
You are the {role}, a specialist supporting the Chief of Staff Agent.

You receive structured assignments from the Chief of Staff Agent. Perform only
work that falls within your role and skills. Return your findings to the Chief
of Staff rather than presenting yourself as the final decision-maker.

Requirements:

- Follow the relevant skill instructions provided below.
- Use only evidence available in the assignment or accessible through approved
  tools.
- Never fabricate evidence, policies, costs, dates, findings, or decisions.
- Clearly distinguish facts, estimates, and assumptions.
- Identify missing information and material limitations.
- Escalate matters outside your authority.
- Always return the required SpecialistResponse structure.
- Preserve the assignment_id supplied by the Chief of Staff.

Available skills:

{skill_instructions}
""".strip()


def create_specialist_agents() -> dict[str, Agent]:
    """Create and return the four specialist agents."""

    innovation_agent = Agent(
        name="Innovation Agent",
        instructions=build_specialist_instructions(
            "innovation-agent",
            "Innovation Agent",
        ),
        output_type=SpecialistResponse,
    )

    compliance_agent = Agent(
        name="Compliance Agent",
        instructions=build_specialist_instructions(
            "compliance-agent",
            "Compliance Agent",
        ),
        output_type=SpecialistResponse,
    )

    project_management_agent = Agent(
        name="Project Management Agent",
        instructions=build_specialist_instructions(
            "project-management-agent",
            "Project Management Agent",
        ),
        output_type=SpecialistResponse,
    )

    data_analyst_agent = Agent(
        name="Data Analyst Agent",
        instructions=build_specialist_instructions(
            "data-analyst-agent",
            "Data Analyst Agent",
        ),
        output_type=SpecialistResponse,
    )

    return {
        "innovation-agent": innovation_agent,
        "compliance-agent": compliance_agent,
        "project-management-agent": project_management_agent,
        "data-analyst-agent": data_analyst_agent,
    }
