"""Streamlit interface for the Chief of Staff multi-agent system."""

import os

import streamlit as st

from orchestrator import run_chief_of_staff


st.set_page_config(
    page_title="Chief of Staff Multi-Agent Assistant",
    page_icon="🧭",
    layout="wide",
)


def configure_openai_key() -> bool:
    """Load the OpenAI API key from Streamlit secrets or the environment."""

    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    return bool(os.getenv("OPENAI_API_KEY"))


def display_consulted_specialists(
    specialists: list[dict],
) -> None:
    """Display the specialists and skill sets used during the run."""

    st.subheader("Orchestration Summary")

    if not specialists:
        st.info(
            "The Chief of Staff answered directly without consulting "
            "a specialist agent."
        )
        return

    st.write(
        f"The Chief of Staff consulted "
        f"{len(specialists)} specialist agent(s)."
    )

    columns = st.columns(len(specialists))

    for column, specialist in zip(columns, specialists):
        with column:
            st.markdown(f"#### {specialist['agent']}")
            st.caption("Skill set loaded for this consultation")

            for skill in specialist.get("skills", []):
                st.markdown(f"- {skill}")


st.title("Chief of Staff Multi-Agent Assistant")

st.caption(
    "The Chief of Staff evaluates your request and consults the Innovation, "
    "Compliance, Project Management, and Data Analyst agents when needed."
)

st.info(
    "This is a decision-support prototype. Agent findings must be reviewed "
    "before they are treated as organizational, legal, financial, or "
    "operational decisions."
)

if not configure_openai_key():
    st.error(
        "The OPENAI_API_KEY secret has not been configured. "
        "Add it through Streamlit's secure secrets settings."
    )
    st.stop()

executive_request = st.text_area(
    "What would you like the Chief of Staff Agent to evaluate?",
    height=180,
    placeholder=(
        "Example: Should we pilot an AI assistant that summarizes executive "
        "meeting materials and tracks follow-up actions?"
    ),
)

if st.button(
    "Run Chief of Staff Analysis",
    type="primary",
    use_container_width=True,
):
    if not executive_request.strip():
        st.warning("Enter a request before running the analysis.")
    else:
        try:
            with st.spinner(
                "The Chief of Staff is consulting the appropriate agents..."
            ):
                run_result = run_chief_of_staff(executive_request)

            display_consulted_specialists(
                run_result["consulted_specialists"]
            )

            st.divider()
            st.subheader("Chief of Staff Response")
            st.markdown(run_result["response"])

        except Exception as exc:
            st.error(
                "The multi-agent analysis could not be completed. "
                f"Technical details: {exc}"
            )
