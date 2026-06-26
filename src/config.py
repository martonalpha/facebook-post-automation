"""Central configuration. Secrets are read from the environment (.env)."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Paths are resolved from the project root so the bot runs from any directory.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "nevnapok.json"
BACKGROUNDS_DIR = BASE_DIR / "assets" / "backgrounds"
FONT_FILE = BASE_DIR / "assets" / "fonts" / "GreatVibes-Regular.ttf"
OUTPUT_DIR = BASE_DIR / "output"

# Facebook Graph API credentials. Never hard-code these.
PAGE_ID = os.getenv("FB_PAGE_ID", "")
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN", "")
GRAPH_API_VERSION = os.getenv("FB_GRAPH_API_VERSION", "v17.0")

# Image settings.
GREETING_TEXT = os.getenv("GREETING_TEXT", "Boldog névnapot")
FONT_SIZE = int(os.getenv("FONT_SIZE", "70"))
TEXT_COLOR = (0, 0, 0)
