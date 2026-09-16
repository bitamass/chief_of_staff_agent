"""Chief of Staff multi-agent orchestration."""

from collections.abc import Mapping
from typing import Any

from agents import Agent, Runner, WebSearchTool

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


EXTERNAL_INTELLIGENCE_INSTRUCTIONS = """
External intelligence is enabled for this request.

Use web search only when current public information would materially improve
the analysis. Appropriate examples include:

- Recent laws, regulations, policies, and official guidance
- Current market or industry developments
- Recent technology changes
- Public organizational announcements
- Current events that may affect a meeting or decision

External intelligence rules:

- Never include confidential, internal, personal, privileged, restricted, or
  unpublished organizational information in a web-search query.
- Search only public information.
- Prefer primary and authoritative sources, such as government agencies,
  official organizational websites, regulatory bodies, research institutions,
  and original reports.
- Confirm important claims using more than one reliable source when practical.
- Clearly distinguish verified external facts from assumptions, analysis, and
  recommendations.
- Identify conflicting, incomplete, uncertain, or outdated information.
- Include relevant publication dates or event dates.
- Do not imply that public information represents internal organizational facts.
- Do not treat search results as formal legal, compliance, financial, medical,
  security, or organizational approval.
- Include a section titled "External intelligence findings" when search results
  materially affect the response.
- Include a final section titled "External sources" containing clickable
  Markdown links and publication dates, when available, for every external
  source used.
- If current external information is unnecessary, do not search merely because
  the tool is available.
""".strip()


def create_chief_of_staff_agent(
    include_external_intelligence: bool = False,
) -> Agent:
    """Create the Chief of Staff with specialists and optional web search."""

    specialists = create_specialist_agents()

    tools = [
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
                "Consult the Project Management Agent about plans about plans, "
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
    ]

    instructions = CHIEF_OF_STAFF_INSTRUCTIONS

    if include_external_intelligence:
        tools.append(
            WebSearchTool(
                search_context_size="medium",
            )
        )
        instructions = (
            CHIEF_OF_STAFF_INSTRUCTIONS
            + "\n\n"
            + EXTERNAL_INTELLIGENCE_INSTRUCTIONS
        )

    return Agent(
        name="Chief of Staff Agent",
        instructions=instructions,
        tools=tools,
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


def _used_external_intelligence(result: Any) -> bool:
    """Determine whether web search was used during the run."""

    for item in result.new_items:
        item_type = _raw_field(item, "type")

        if item_type == "web_search_call":
            return True

    return False


def run_chief_of_staff(
    request: str,
    include_external_intelligence: bool = False,
) -> dict[str, Any]:
    """Run a request and return the response with orchestration metadata."""

    if not request or not request.strip():
        raise ValueError("A request is required.")

    chief_of_staff = create_chief_of_staff_agent(
        include_external_intelligence=include_external_intelligence,
    )

    result = Runner.run_sync(
        chief_of_staff,
        request.strip(),
    )

    return {
        "response": str(result.final_output),
        "consulted_specialists": _get_consulted_specialists(result),
        "external_intelligence_enabled": include_external_intelligence,
        "external_intelligence_used": _used_external_intelligence(result),
    }
