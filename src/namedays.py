"""Look up Hungarian name days from the bundled JSON data set.

The data is stored as `{ month: { day: { "main": [...], "other": [...] } } }`
where months and days are non-zero-padded strings (e.g. "1" not "01").
"""

import json
from datetime import date

from . import config


def load_namedays() -> dict:
    """Load and return the full name-day data set."""
    with open(config.DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def main_names_for(day: date, namedays: dict | None = None) -> list[str]:
    """Return the list of "main" name-day names for the given date.

    Returns an empty list if there is no main name day on that date.
    """
    if namedays is None:
        namedays = load_namedays()
    month_key = str(day.month)
    day_key = str(day.day)
    return namedays.get(month_key, {}).get(day_key, {}).get("main", [])
