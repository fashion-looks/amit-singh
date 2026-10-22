# Mind-to-Starlight: EEG-ready Galaxy Controller

A runnable prototype that maps a manual focus slider to a simulated galaxy visualizer. No EEG headset is connected in this version.

## Automation included

- CI when files under `mind-starlight/**` change: Python syntax checks, Flask route smoke tests, and a downloadable source artifact.
- Daily scheduled maintenance checks at 03:17 UTC and manual `workflow_dispatch`.
- Dependabot weekly updates for Python dependencies and GitHub Actions.
- `/healthz` endpoint for hosting health checks and external uptime monitors.
- `Procfile` for Gunicorn-based hosting.

## Run locally

Requires Python 3.10+.

```bash
cd mind-starlight
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Open http://127.0.0.1:5000.

Production-style command:
```bash
gunicorn app:app --bind 0.0.0.0:8000
```

## Make it available 24/7

GitHub Actions automates checks and maintenance; it does **not** host a web server continuously. To make this app available all day, deploy it to a Python web host or VPS. For a hosting provider connected to GitHub:

1. Connect this repository.
2. Set the service root directory to `mind-starlight`.
3. Use start command `gunicorn app:app --bind 0.0.0.0:$PORT`.
4. Optionally set `NASA_API_KEY` as a hosting environment variable. Without a key, `DEMO_KEY` is used and has strict rate limits.
5. Configure an external uptime monitor to request `https://YOUR-HOST/healthz` after deployment.

Free-tier hosts may sleep, have usage limits, or cold starts; true uninterrupted service depends on the host plan. A health endpoint reports app status, not the availability of NASA.

## Security

- Keep your real API key in a host environment variable or a GitHub Actions secret; do not commit it.
- GitHub Actions must be enabled in repository settings for scheduled workflows.
- Scheduled workflows are best-effort and may be delayed by GitHub.
- The focus slider is a simulation input, not a brain signal. Live EEG requires a chosen compatible headset and device-specific SDK or data stream integration.

## License

MIT.
