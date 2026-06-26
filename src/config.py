"""Central configuration.

All secrets are read from environment variables so that nothing sensitive
ever ends up in the source code or in version control. During local
development the variables are loaded from a `.env` file (see `.env.example`).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load variables from a local .env file if it exists. In production
# (e.g. a server or CI) the variables can also come from the real environment.
load_dotenv()

# --- Project paths -------------------------------------------------------
# Everything is resolved relative to the project root, so the bot works no
# matter which directory it is started from (handy for cron / Task Scheduler).
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "nevnapok.json"
BACKGROUNDS_DIR = BASE_DIR / "assets" / "backgrounds"
FONT_FILE = BASE_DIR / "assets" / "fonts" / "GreatVibes-Regular.ttf"
OUTPUT_DIR = BASE_DIR / "output"

# --- Facebook Graph API credentials --------------------------------------
# NEVER hard-code these. Put them in your .env file (which is git-ignored).
PAGE_ID = os.getenv("FB_PAGE_ID", "")
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN", "")
GRAPH_API_VERSION = os.getenv("FB_GRAPH_API_VERSION", "v17.0")

# --- Image settings ------------------------------------------------------
GREETING_TEXT = os.getenv("GREETING_TEXT", "Boldog névnapot")
FONT_SIZE = int(os.getenv("FONT_SIZE", "70"))
TEXT_COLOR = (0, 0, 0)  # black
