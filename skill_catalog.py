"""Discover the Chief of Staff capability and skill hierarchy from the repo."""

from pathlib import Path


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


def discover_capabilities(repo_root):
    """Return capability labels and child skills discovered from GitHub folders."""
    repo_root = Path(repo_root)
    discovered = {}
    for capability_dir in sorted(repo_root.iterdir() if repo_root.exists() else []):
        if not capability_dir.is_dir() or not capability_dir.name[:2].isdigit():
            continue
        skills = sorted(
            display_name(child.name)
            for child in capability_dir.iterdir()
            if child.is_dir() and not child.name.startswith(".")
        )
        if skills:
            discovered[display_name(capability_dir.name)] = skills
    return discovered or FALLBACK_CAPABILITIES


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
