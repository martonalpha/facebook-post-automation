# Facebook Post Automation

A small Python automation that generates a Hungarian name-day greeting image
and posts it to a Facebook Page once a day, automatically.

In Hungary every day of the year is tied to one or more first names
("névnap" = name day), and congratulating people on their name day is a small
tradition. The bot looks up today's name, draws a greeting card and publishes it.

## Why I built it (and what I learned)

This was an experiment to see whether I could build a complete, hands-off
automation end to end. Hungarian name days were a perfect fit — there is a name
to celebrate every single day — so it became a steady daily content source.

How it runs:

- The code is deployed to **GitHub Actions** and runs once a day, on its own.
- Each run first **generates the image** for that day's name day (currently
  Hungarian, but the same approach works for Slovak, Czech or any other dataset),
  then **posts the generated image to Facebook**.
- No server to maintain — GitHub runs it on a schedule and the secrets live in
  repository secrets.

**The main lesson:** Facebook doesn't like automation. Bot-style posting gets
deprioritized, so the algorithm won't recommend the page to many people and
organic reach stays very low. So this isn't a growth hack — it's a finished
learning project, and I'm sharing it as a clean example of scheduled automation,
image generation and the Graph API.

## Use cases

- 🎉 **Name-day / birthday greetings** posted automatically to a page.
- 🌍 **Other languages or countries** — swap `data/nevnapok.json` for a Slovak,
  Czech or any other dataset; the pipeline stays the same.
- 🗓️ **Any "one post per day" content** (quotes, tips, "on this day" facts) by
  changing what the image draws and what `main.py` looks up.
- 🧩 **A template for scheduled Graph API posting** in your own projects.

## How it works

```
date.today()  ->  look up name in nevnapok.json  ->  draw greeting image  ->  post to Facebook
```

| File | Responsibility |
|------|----------------|
| `main.py` | Daily entry point: today's name → image → Facebook post |
| `generate_all.py` | Utility: render every name day to `output/` (no posting) |
| `src/config.py` | Loads all settings/secrets from the environment (`.env`) |
| `src/namedays.py` | Loads the JSON data and looks up names for a date |
| `src/image.py` | Generates the greeting image (random background + centered text) |
| `src/facebook.py` | Uploads a photo to a Facebook Page via the Graph API |

## Setup

1. **Clone and enter the project**

   ```bash
   git clone https://github.com/martonalpha/facebook-post-automation.git
   cd facebook-post-automation
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Configure your secrets**

   Copy the example file and fill in your own values:

   ```bash
   cp .env.example .env
   ```

   ```ini
   FB_PAGE_ID=put_your_facebook_page_id_here
   FB_ACCESS_TOKEN=put_your_facebook_page_access_token_here
   ```

   The `.env` file is git-ignored, so your token never ends up on GitHub.

### Getting a Facebook Page access token

1. Create a Facebook App at <https://developers.facebook.com/>.
2. Use the **Graph API Explorer** to generate a Page access token with the
   `pages_manage_posts` and `pages_read_engagement` permissions:
   <https://developers.facebook.com/tools/explorer/>.
3. Exchange it for a **long-lived token** so it doesn't expire after a few hours.
4. Put the token and your numeric Page ID into `.env`.

> ⚠️ **Never commit a real token.** If a token ever leaks, revoke it in the
> Facebook developer dashboard and generate a new one.

## Usage

Preview the images locally (no posting needed):

```bash
python generate_all.py
```

Generate and post today's greeting:

```bash
python main.py
```

## Running it daily

### GitHub Actions (how I deployed it)

The repo includes [`.github/workflows/daily-post.yml`](.github/workflows/daily-post.yml),
which runs `main.py` once a day in the cloud — no server needed.

1. In your repository go to **Settings → Secrets and variables → Actions** and
   add `FB_PAGE_ID` and `FB_ACCESS_TOKEN` as repository secrets.
2. Adjust the `cron` time in the workflow if you like (it is in UTC).

You can also trigger a run manually from the **Actions** tab to test it.

### Locally with cron / Task Scheduler

**Linux / macOS (cron)** — post every day at 08:00:

```cron
0 8 * * * cd /path/to/facebook-post-automation && /path/to/.venv/bin/python main.py >> bot.log 2>&1
```

**Windows (Task Scheduler):** create a Basic Task that runs daily, points to
`.venv\Scripts\python.exe` with `main.py` as the argument, and set "Start in"
to the project folder.

## Credits

- **Name-day data** (`data/nevnapok.json`) comes from the
  [froccsos/nevnapok-json](https://github.com/froccsos/nevnapok-json) project
  (MIT License). Original source of the list:
  <https://mek.oszk.hu/00000/00056/html/196.htm>.
- **Font:** [Great Vibes](https://fonts.google.com/specimen/Great+Vibes),
  licensed under the SIL Open Font License (see `assets/fonts/OFL.txt`).

## License

This project's source code is released under the [MIT License](LICENSE).
The bundled data and font keep their own respective licenses noted above.
