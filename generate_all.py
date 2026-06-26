"""Utility: generate greeting images for every name day, without posting.

Handy for previewing how the images look before wiring up Facebook.
Images are written to the `output/` directory as `MM-DD-Name.png`.
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
            output_path = config.OUTPUT_DIR / f"{int(month):02d}-{int(day):02d}-{name}.png"
            image.create_greeting_image(name, output_path)
            count += 1

    print(f"Generated {count} images in {config.OUTPUT_DIR}.")


if __name__ == "__main__":
    main()
