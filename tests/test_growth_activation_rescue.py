import json
from pathlib import Path

PACKAGE = Path("workflow_packages/growth.activation_rescue")
MANIFEST = PACKAGE / "workflow.json"

def test_package_contract():
    data = json.loads(MANIFEST.read_text())
    d = data["definition"]
    assert d["key"] == "growth.activation_rescue"
    assert d["executor"] == "codex.procedure"
    assert d["schedule_modes"] == ["on_demand", "weekly"]
    assert d["input_schema"]["additionalProperties"] is False
    assert "project_id" in d["input_schema"]["required"]
    assert "cohort_file" in d["input_schema"]["required"]
    assert "activation_event" in d["input_schema"]["required"]
    assert d["procedure"]["output"]["path"] == "reports/ACTIVATION_RESCUE.md"
    assert d["procedure"]["entry_skill"] == "activation-rescue"

def test_resources_are_declared_and_present():
    d = json.loads(MANIFEST.read_text())["definition"]["procedure"]
    assert (PACKAGE / d["prompt_path"]).is_file()
    for resource in d["skill_files"]:
        assert (PACKAGE / resource).is_file()

def test_prompt_is_single_outcome():
    prompt = (PACKAGE / "PROMPT.md").read_text()
    assert "exactly ONE concrete marketing action" in prompt
    assert "Do not produce a list of five tactics" in prompt

def test_skill_requires_evidence():
    skill = (PACKAGE / "skills/activation-rescue/SKILL.md").read_text()
    assert "Never claim the campaign will improve activation" in skill
    assert "Do not infer demographics" in skill
    assert "Diagnosed leak" in skill
