"""Generate a name-day greeting image: random background + centered text."""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from . import config


def list_backgrounds() -> list[Path]:
    backgrounds = sorted(config.BACKGROUNDS_DIR.glob("*.png"))
    if not backgrounds:
        raise FileNotFoundError(f"No background images found in {config.BACKGROUNDS_DIR}")
    return backgrounds


def _line_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    return right - left, bottom - top


def create_greeting_image(name: str, output_path: Path, background_path: Path | None = None) -> Path:
    """Render a greeting for `name` and save it. Picks a random background if none given."""
    if background_path is None:
        background_path = random.choice(list_backgrounds())

    img = Image.open(background_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(config.FONT_FILE), config.FONT_SIZE)

    lines = [config.GREETING_TEXT, name]
    sizes = [_line_size(draw, line, font) for line in lines]

    # Center the two-line text block based on the actual image size.
    y = (img.height - sum(height for _, height in sizes)) // 2
    for line, (width, height) in zip(lines, sizes):
        draw.text(((img.width - width) // 2, y), line, font=font, fill=config.TEXT_COLOR)
        y += height

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)
    return output_path
