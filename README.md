# Facebook Name-Day Bot 🎉

A small Python automation that, **once a day**, generates a Hungarian name-day
greeting image and posts it to a Facebook Page via the Graph API.

In Hungary every day of the year is associated with one or more first names
("névnap" = name day), and it is a tradition to congratulate people on their
name day. This bot turns that tradition into an automatic daily Facebook post:
it looks up today's name, draws a nice greeting card, and publishes it.

> **A note on reach / why I'm sharing this anyway**
>
> I originally ran this bot to post automatically every day at a fixed time.
> It works, but Facebook actively deprioritizes automated / bot-style posting,
> so a page fed only by this script will get very little organic reach — Facebook
> simply won't recommend it to many people. So this is **not** a growth hack;
> it's a fun little learning project about image generation + the Graph API.
> I'm publishing it in case it's useful to someone as an example. 🙂

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

## Scheduling a daily post

The bot posts whatever the current date's name day is, so you just need to run
`main.py` once per day at your preferred time.

**Linux / macOS (cron)** — post every day at 08:00:

```cron
0 8 * * * cd /path/to/facebook-nameday-bot && /path/to/.venv/bin/python main.py >> bot.log 2>&1
```

**Windows (Task Scheduler):** create a Basic Task that runs daily at 08:00 and
points to `.venv\Scripts\python.exe` with `main.py` as the argument, and set
"Start in" to the project folder.

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
