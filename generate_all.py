"""Render a greeting image for every name day (no posting). Useful for previewing.

Output files are written to `output/` as `MM-DD-Name.png`.
"""

from src import config, image, namedays


def main() -> None:
    data = namedays.load_namedays()
    count = 0
    for month in sorted(data, key=int):
        for day in sorted(data[month], key=int):
            names = data[month][day].get("main", [])
            if not names:
                continue
            name = names[0]
            image.create_greeting_image(name, config.OUTPUT_DIR / f"{int(month):02d}-{int(day):02d}-{name}.png")
            count += 1
    print(f"Generated {count} images in {config.OUTPUT_DIR}.")


if __name__ == "__main__":
    main()
