# Mind-to-Starlight: EEG-ready Galaxy Controller

A real, runnable prototype for controlling an animated galaxy with a **manual focus input today**, with a clearly separated adapter point for future EEG hardware integration.

## What works now

- Responsive browser-based animated galaxy visualizer.
- Manual focus slider that changes galaxy motion/glow.
- Browser microphone/voice commands are optional enhancement? (not required for the main demo).
- Flask backend and NASA APOD endpoint remain available in `app.py`.
- No EEG hardware is required to try the visualizer.

## What does not work yet

Because no EEG headset is available, the app cannot read brainwaves today. The focus slider is explicitly a **simulation**, not a physiological measurement. To use live brain signals, choose a specific EEG headset, install its supported SDK/streaming tool, and implement the vendor-specific adapter. This project does not claim that thought can physically control stars, Earth, or the universe.

## Run locally

Requires Python 3.10+.

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Open http://127.0.0.1:5000. The NASA panel calls the APOD API; `DEMO_KEY` is rate-limited. A NASA key is optional and can be put in your local `.env` file. Never commit a real key.

## Try the galaxy controller

1. Open the page and find **Galaxy Control — Simulated Input**.
2. Drag the focus slider from low to high and observe the glow and orbital speed change.
3. Use the **Reset** button to return to the default settings.
4. Optionally click **Load NASA astronomy image** to test the API integration.

## Future EEG connection

Integrate this in three deliberate steps:
1. Select the actual device and its supported SDK/stream protocol.
2. Write a backend adapter that validates incoming numeric values and converts a measured, documented signal feature into a normalized control value.
3. Replace the manual slider as the source of the control value only after device streaming has been tested. Keep a manual fallback and show the sensor connection state.

Do not invent a universal EEG interface: each device and SDK is different.

## Automated checks

GitHub Actions runs a Python syntax check and a basic Flask route smoke test on pushes and pull requests.

## License

MIT.
