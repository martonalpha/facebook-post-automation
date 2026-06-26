"""Publish a photo to a Facebook Page using the Graph API."""

from pathlib import Path

import requests

from . import config


def post_photo(image_path: Path, message: str) -> dict:
    """Upload `image_path` with `message` to the configured Page and return the API response."""
    if not config.PAGE_ID or not config.ACCESS_TOKEN:
        raise RuntimeError("Missing credentials: set FB_PAGE_ID and FB_ACCESS_TOKEN in your .env file.")

    url = f"https://graph.facebook.com/{config.GRAPH_API_VERSION}/{config.PAGE_ID}/photos"
    data = {"access_token": config.ACCESS_TOKEN, "message": message}

    with open(image_path, "rb") as image_file:
        response = requests.post(url, data=data, files={"source": image_file})

    response.raise_for_status()
    return response.json()
