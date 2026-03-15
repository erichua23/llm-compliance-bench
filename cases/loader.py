"""Load and filter test cases from YAML."""

import os
import yaml


def load_cases(category: str | None = None, difficulty: str | None = None) -> list[dict]:
    cases_file = os.path.join(os.path.dirname(__file__), "test_cases.yaml")
    with open(cases_file) as f:
        cases = yaml.safe_load(f)

    if category:
        cases = [c for c in cases if c["category"] == category]
    if difficulty:
        cases = [c for c in cases if c["difficulty"] == difficulty]
    return cases
