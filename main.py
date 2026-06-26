"""Daily entry point.

Looks up today's Hungarian name day, generates a greeting image and posts
it to the configured Facebook Page. This is the script you schedule to run
once a day (see the README for cron / Task Scheduler examples).
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
    output_path = config.OUTPUT_DIR / f"{today:%m-%d}.png"
    image.create_greeting_image(name, output_path)
    print(f"Image generated: {output_path}")

    result = facebook.post_photo(output_path, f"Boldog névnapot, {name}!")
    post_id = result.get("post_id") or result.get("id", "?")
    print(f"Posted to Facebook (id: {post_id}).")


if __name__ == "__main__":
    main()
