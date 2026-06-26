"""Look up Hungarian name days from the bundled JSON data set.

Data layout: { month: { day: { "main": [...], "other": [...] } } } where
month/day keys are non-zero-padded strings (e.g. "1", not "01").
"""

import json
from datetime import date

from . import config


def load_namedays() -> dict:
    """Load and return the full name-day data set."""
    with open(config.DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def main_names_for(day: date, namedays: dict | None = None) -> list[str]:
    """Return the "main" names for the given date, or an empty list if none."""
    if namedays is None:
        namedays = load_namedays()
    return namedays.get(str(day.month), {}).get(str(day.day), {}).get("main", [])
