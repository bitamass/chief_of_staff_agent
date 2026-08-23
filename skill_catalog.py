"""Discover the Chief of Staff capability and skill hierarchy from the repo."""

from pathlib import Path
import re


# Used only when the capability folders are not present in a standalone demo
# package. In GitHub/Streamlit, discovery reads the repository folders directly.
FALLBACK_CAPABILITIES = {
    "02 Weekly and Daily Meeting Intelligence": [
        "Action Item Management",
        "Calendar Prioritization",
        "Create Agendas",
        "Follow Up On Commitments",
        "Meeting Preparation",
        "Prepare Pre-Meeting Briefing Materials",
        "Summarize Prior Discussions",
        "Track Decisions",
    ],
    "03 Decision Support": [
        "Alternative And Recommendation Generation",
        "Decision Logs",
        "Trade Off Analysis",
    ],
    "04 Initiative Strategic Alignment": [
        "Initiative Portfolio Review",
        "Map Initiatives To Strategic Objectives",
        "OKR Alignment",
        "Priority Conflict Detection",
    ],
}


def display_name(folder_name):
    """Convert a repository folder name into a readable label."""
    return folder_name.replace("_", " ").strip()


def _normalized(value):
    """Return a stable key for matching repository and display names."""
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _read_instruction_files(skill_dir):
    """Read the documented contract for one repository skill."""
    filenames = (
        "SKILL.md",
        "README.md",
        "INPUTS.md",
        "WORKFLOW.md",
        "OUTPUTS.md",
        "PROMPT.md",
        "EVALUATION.md",
    )
    documents = {}
    for filename in filenames:
        path = skill_dir / filename
        if path.is_file():
            try:
                documents[filename] = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                documents[filename] = path.read_text(encoding="utf-8", errors="replace")
    return documents


def discover_skill_catalog(repo_root):
    """Discover skills and read their definition files from the deployed repo.

    Streamlit deploys a checkout of the GitHub repository, so this performs no
    network request and requires no GitHub token. The returned catalog retains
    repository paths and instruction text for traceability.
    """
    repo_root = Path(repo_root)
    catalog = {}
    for capability_dir in sorted(repo_root.iterdir() if repo_root.exists() else []):
        if not capability_dir.is_dir() or not capability_dir.name[:2].isdigit():
            continue
        capability_label = display_name(capability_dir.name)
        skills = {}
        for skill_dir in sorted(capability_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                continue
            skill_label = display_name(skill_dir.name)
            skills[skill_label] = {
                "capability": capability_label,
                "name": skill_label,
                "repository_path": str(skill_dir.relative_to(repo_root)),
                "documents": _read_instruction_files(skill_dir),
                "connected": skill_label in CONNECTED_SKILLS,
                "source": "repository",
            }
        if skills:
            catalog[capability_label] = skills

    if catalog:
        return catalog

    # The fallback keeps a downloaded standalone demo usable, but makes clear
    # that no repository instruction files were found in that package.
    return {
        capability: {
            skill: {
                "capability": capability,
                "name": skill,
                "repository_path": None,
                "documents": {},
                "connected": skill in CONNECTED_SKILLS,
                "source": "fallback",
            }
            for skill in skills
        }
        for capability, skills in FALLBACK_CAPABILITIES.items()
    }


def discover_capabilities(repo_root):
    """Return capability labels and child skills discovered from GitHub folders."""
    catalog = discover_skill_catalog(repo_root)
    return {capability: list(skills) for capability, skills in catalog.items()}


CONNECTED_SKILLS = {
    "Action Item Management",
    "Calendar Prioritization",
    "Create Agendas",
    "Follow Up On Commitments",
    "Meeting Preparation",
    "Prepare Pre-Meeting Briefing Materials",
    "Summarize Prior Discussions",
    "Track Decisions",
    "Decision Logs",
    "Initiative Portfolio Review",
}
