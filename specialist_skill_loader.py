"""Load specialist-agent skills from their public GitHub repositories."""

import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT_DIR = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT_DIR / "config" / "specialist-agents.json"


class SpecialistSkillError(RuntimeError):
    """Raised when specialist configuration or skill loading fails."""


def load_agent_registry() -> dict:
    """Load the specialist-agent registry."""

    try:
        with REGISTRY_PATH.open("r", encoding="utf-8") as registry_file:
            return json.load(registry_file)
    except FileNotFoundError as exc:
        raise SpecialistSkillError(
            f"Agent registry was not found: {REGISTRY_PATH}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise SpecialistSkillError(
            f"Agent registry contains invalid JSON: {exc}"
        ) from exc


def get_agent_config(agent_id: str) -> dict:
    """Return the registry entry for one specialist agent."""

    registry = load_agent_registry()

    for agent in registry.get("specialist_agents", []):
        if agent.get("id") == agent_id:
            return agent

    raise SpecialistSkillError(
        f"Unknown specialist agent: {agent_id}"
    )


def build_skill_url(repository: str, skill_name: str) -> str:
    """Build the raw GitHub URL for a specialist SKILL.md file."""

    repository_path = repository.removeprefix(
        "https://github.com/"
    ).rstrip("/")

    return (
        f"https://raw.githubusercontent.com/"
        f"{repository_path}/main/"
        f".agents/skills/{skill_name}/SKILL.md"
    )


def download_skill(repository: str, skill_name: str) -> str:
    """Download one SKILL.md file from GitHub."""

    skill_url = build_skill_url(repository, skill_name)
    request = Request(
        skill_url,
        headers={
            "User-Agent": "chief-of-staff-agent"
        }
    )

    try:
        with urlopen(request, timeout=10) as response:
            return response.read().decode("utf-8")
    except HTTPError as exc:
        raise SpecialistSkillError(
            f"GitHub returned HTTP {exc.code} for "
            f"{skill_name}: {skill_url}"
        ) from exc
    except URLError as exc:
        raise SpecialistSkillError(
            f"Could not load {skill_name}: {exc.reason}"
        ) from exc


def load_agent_skills(agent_id: str) -> str:
    """Load and combine every skill owned by one specialist agent."""

    agent = get_agent_config(agent_id)
    repository = agent["repository"]
    skill_documents = []

    for skill_name in agent.get("skills", []):
        skill_content = download_skill(
            repository=repository,
            skill_name=skill_name,
        )

        skill_documents.append(
            f"# Loaded skill: {skill_name}\n\n{skill_content}"
        )

    if not skill_documents:
        raise SpecialistSkillError(
            f"No skills are registered for {agent_id}."
        )

    return "\n\n---\n\n".join(skill_documents)
