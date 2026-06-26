"""Daily entry point: post today's name-day greeting to Facebook.

Schedule this to run once a day (see the README for cron / Task Scheduler).
"""

from datetime import date

from src import config, facebook, image, namedays


def main() -> None:
    today = date.today()
    names = namedays.main_names_for(today)
    if not names:
        print(f"No main name day for {today:%m-%d} - nothing to post.")
        return

    name = names[0]
    output_path = image.create_greeting_image(name, config.OUTPUT_DIR / f"{today:%m-%d}.png")
    print(f"Image generated: {output_path}")

    result = facebook.post_photo(output_path, f"Boldog névnapot, {name}!")
    print(f"Posted to Facebook (id: {result.get('post_id') or result.get('id', '?')}).")


if __name__ == "__main__":
    main()
