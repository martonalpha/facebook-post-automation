"""Generate a name-day greeting image.

A random background is picked from `assets/backgrounds`, and two centered
lines of text are drawn on it: the greeting and the name.
"""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from . import config


def list_backgrounds() -> list[Path]:
    """Return all available background images, sorted by file name."""
    backgrounds = sorted(config.BACKGROUNDS_DIR.glob("*.png"))
    if not backgrounds:
        raise FileNotFoundError(f"No background images found in {config.BACKGROUNDS_DIR}")
    return backgrounds


def _line_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    """Return the (width, height) of a single line of text."""
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    return right - left, bottom - top


def create_greeting_image(name: str, output_path: Path, background_path: Path | None = None) -> Path:
    """Create a greeting image for `name` and save it to `output_path`.

    If `background_path` is not given, a random background is chosen.
    The two lines of text are centered horizontally and vertically based on
    the actual image size, so backgrounds of any dimension work.
    """
    if background_path is None:
        background_path = random.choice(list_backgrounds())

    img = Image.open(background_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(config.FONT_FILE), config.FONT_SIZE)

    lines = [config.GREETING_TEXT, name]
    sizes = [_line_size(draw, line, font) for line in lines]
    total_text_height = sum(height for _, height in sizes)

    # Start so that the whole text block is vertically centered.
    y = (img.height - total_text_height) // 2
    for line, (width, height) in zip(lines, sizes):
        x = (img.width - width) // 2
        draw.text((x, y), line, font=font, fill=config.TEXT_COLOR)
        y += height

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path)
    return output_path
