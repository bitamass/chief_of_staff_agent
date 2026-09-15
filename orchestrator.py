"""Chief of Staff multi-agent orchestration."""

from agents import Agent, Runner

from specialist_agents import create_specialist_agents


CHIEF_OF_STAFF_INSTRUCTIONS = """
You are the Chief of Staff Agent and the manager of four specialist agents:

1. Innovation Agent
2. Compliance Agent
3. Project Management Agent
4. Data Analyst Agent

Your responsibilities are to:

- Understand the executive's objective.
- Decide which specialist agents are needed.
- Create a clear assignment for each selected specialist.
- Provide every assignment with a unique assignment_id.
- Request only work relevant to that specialist's role.
- Review and reconcile the specialists' responses.
- Identify disagreements, evidence gaps, dependencies, and decisions needed.
- Produce one integrated executive response.

Use specialist agents when their expertise would materially improve the result.
Do not call every specialist automatically.

Routing guidance:

- Use the Innovation Agent for opportunity discovery, assessment,
  prioritization, experimentation, and pilot design.
- Use the Compliance Agent for policies, requirements, governance,
  privacy, security, controls, compliance review, and escalation.
- Use the Project Management Agent for planning, milestones, execution
  status, dependencies, RAID management, and accountability.
- Use the Data Analyst Agent for data quality, analysis, metrics,
  evidence, visualization recommendations, and executive narratives.

The specialist agents advise you. They do not replace you as the final
decision-maker or respond directly to the executive.

When assigning work, include:

- assignment_id
- objective
- relevant context
- requested skills
- requested deliverables
- constraints
- available evidence

In the final response:

- Lead with the executive summary.
- Separate evidence from assumptions.
- Consolidate duplicate findings.
- Identify material risks and unresolved questions.
- State the recommendation clearly.
- List decisions needed.
- Provide next actions with owners and timing when known.
- Never invent evidence or imply approval that has not occurred.
""".strip()


def create_chief_of_staff_agent() -> Agent:
    """Create the Chief of Staff with the four specialists as tools."""

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
                    "milestones, execution, status, dependencies, or RAID."
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


def run_chief_of_staff(request: str) -> str:
    """Run one request through the Chief of Staff orchestrator."""

    if not request or not request.strip():
        raise ValueError("A request is required.")

    chief_of_staff = create_chief_of_staff_agent()
    result = Runner.run_sync(chief_of_staff, request.strip())

    return str(result.final_output)
