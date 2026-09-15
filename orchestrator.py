"""Chief of Staff multi-agent orchestration."""

from collections.abc import Mapping
from typing import Any

from agents import Agent, Runner

from specialist_agents import create_specialist_agents


SPECIALIST_TOOL_METADATA = {
    "consult_innovation_agent": {
        "agent": "Innovation Agent",
        "skills": [
            "Opportunity discovery",
            "Opportunity assessment and prioritization",
            "Experimentation and implementation",
        ],
    },
    "consult_compliance_agent": {
        "agent": "Compliance Agent",
        "skills": [
            "Requirement and policy mapping",
            "Risk and control assessment",
            "Compliance review and escalation",
        ],
    },
    "consult_project_management_agent": {
        "agent": "Project Management Agent",
        "skills": [
            "Project planning and mobilization",
            "Execution and status management",
            "RAID and decision management",
        ],
    },
    "consult_data_analyst_agent": {
        "agent": "Data Analyst Agent",
        "skills": [
            "Data intake, preparation, and quality",
            "Analysis and insight generation",
            "Visualization and executive narrative",
        ],
    },
}


CHIEF_OF_STAFF_INSTRUCTIONS = """
You are the Chief of Staff Agent and manager of four specialist agents:

1. Innovation Agent
2. Compliance Agent
3. Project Management Agent
4. Data Analyst Agent

Your responsibilities are to:

- Understand the executive's objective.
- Decide which specialist agents are needed.
- Create a clear assignment for each selected specialist.
- Give every assignment a unique assignment_id.
- Review and reconcile the specialists' responses.
- Identify disagreements, evidence gaps, dependencies, and decisions needed.
- Produce one integrated executive response.

Routing guidance:

- Use the Innovation Agent for opportunity discovery, assessment,
  prioritization, experimentation, and pilot design.
- Use the Compliance Agent for policies, requirements, governance,
  privacy, security, controls, reviews, and escalations.
- Use the Project Management Agent for plans, milestones, execution,
  dependencies, RAID management, and accountability.
- Use the Data Analyst Agent for data quality, analysis, metrics,
  evidence, visualizations, and executive narratives.

Use specialists only when their expertise materially improves the answer.
The specialists advise you; you remain responsible for the final response.

When assigning work, include:

- assignment_id
- objective
- relevant context
- requested skills
- requested deliverables
- constraints
- available evidence

Final-response requirements:

- Lead with an executive summary.
- Separate evidence from assumptions.
- Consolidate duplicate findings.
- Identify material risks and unresolved questions.
- State the recommendation clearly.
- List decisions requiring executive approval.
- Provide next actions with owners and timing when known.
- Never invent evidence or imply approval that has not occurred.
- Use concise headings, bullets, and standard Markdown.
- Keep paragraphs short and readable.
- When using a table, include a complete header and separator row.
- Use this exact three-column structure for plans:
  | Timing | Focus | Exit condition |
  |---|---|---|
- Do not combine table headings into a single cell.
""".strip()


def create_chief_of_staff_agent() -> Agent:
    """Create the Chief of Staff with four specialists as tools."""

    specialists = create_specialist_agents()

    return Agent(
        name="Chief of Staff Agent",
        instructions=CHIEF_OF_STAFF_INSTRUCTIONS,
        tools=[
            specialists["innovation-agent"].as_tool(
                tool_name="consult_innovation_agent",
                tool_description=(
                    "Consult the Innovation Agent to discover, assess, "
                    "prioritize, or advance an innovation opportunity."
                ),
            ),
            specialists["compliance-agent"].as_tool(
                tool_name="consult_compliance_agent",
                tool_description=(
                    "Consult the Compliance Agent about requirements, "
                    "policies, risks, controls, reviews, or escalations."
                ),
            ),
            specialists["project-management-agent"].as_tool(
                tool_name="consult_project_management_agent",
                tool_description=(
                    "Consult the Project Management Agent about plans, "
                    "milestones, execution, dependencies, or RAID."
                ),
            ),
            specialists["data-analyst-agent"].as_tool(
                tool_name="consult_data_analyst_agent",
                tool_description=(
                    "Consult the Data Analyst Agent about data quality, "
                    "analysis, metrics, insights, or visualizations."
                ),
            ),
        ],
    )


def _raw_field(item: Any, field_name: str) -> Any:
    """Read a field from an SDK raw item or mapping."""

    raw_item = getattr(item, "raw_item", None)

    if isinstance(raw_item, Mapping):
        return raw_item.get(field_name)

    return getattr(raw_item, field_name, None)


def _get_consulted_specialists(result: Any) -> list[dict[str, Any]]:
    """Identify specialist tools called during the orchestration run."""

    consulted = []
    recorded_tools = set()

    for item in result.new_items:
        tool_name = _raw_field(item, "name")

        if (
            tool_name in SPECIALIST_TOOL_METADATA
            and tool_name not in recorded_tools
        ):
            consulted.append(
                SPECIALIST_TOOL_METADATA[tool_name].copy()
            )
            recorded_tools.add(tool_name)

    return consulted


def run_chief_of_staff(request: str) -> dict[str, Any]:
    """Run a request and return the response with orchestration metadata."""

    if not request or not request.strip():
        raise ValueError("A request is required.")

    chief_of_staff = create_chief_of_staff_agent()

    result = Runner.run_sync(
        chief_of_staff,
        request.strip(),
    )

    return {
        "response": str(result.final_output),
        "consulted_specialists": _get_consulted_specialists(result),
    }
