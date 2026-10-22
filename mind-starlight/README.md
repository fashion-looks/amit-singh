# Mind ↔ Starlight — Space Data Demo

A beginner-friendly demo matching the automatic flow:

**EEG device (optional) → Python processing → Internet/API → Space data → Visualization**

## What works in this project

- Mobile-friendly animated starfield and responsive interface.
- Manual focus slider as a **simulation input**.
- Python/Flask backend fetching NASA Astronomy Picture of the Day (APOD).
- GitHub Actions workflow for Python syntax and route smoke checks.

## Scientific limitations

This demo does **not** read actual brainwaves, control Earth, stars or the universe. The focus slider is not an EEG signal. Actual EEG requires compatible hardware, its SDK, and device-specific integration. NASA APOD supplies astronomy content, not a real-time feed of every star.

## Run locally

Requires Python 3.10 or later.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
# Optional: add your NASA API key to .env
python app.py
```

Open http://127.0.0.1:5000.

Get an optional key at https://api.nasa.gov/. Without a key, the app uses `DEMO_KEY`, which is rate-limited.

## Secrets for GitHub Actions

If adapting this project to use a private key in CI, add it in **Settings → Secrets and variables → Actions** as `NASA_API_KEY`. Never commit your real `.env` file or key.

## License

MIT.
