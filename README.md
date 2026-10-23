# Amit Singh — All-in-One Starter Kit

A mobile-friendly foundation for small business workflows, personal productivity, and technology experiments. This repository is a curated starter kit—not literally every kind of code that exists.

## Included
- Responsive dashboard in plain HTML/CSS/JavaScript
- Local task tracker with browser storage
- CSV export for tasks
- Basic automated tests (Node.js built-in test runner)
- GitHub Actions CI on pushes and pull requests, plus a scheduled weekly check
- Security and contribution guidance

## Run locally
No build tools or dependencies are needed for the web dashboard. Open `index.html` in a modern browser, or serve this folder with any static HTTP server.

For automated tests, install Node.js 20 or newer, then run:

```bash
npm test
```

## Publish with GitHub Pages
1. Open **Settings → Pages**.
2. Select **Deploy from a branch**.
3. Select branch `feat/at-a-glance-starter-kit` and folder `/ (root)`, then save.
4. Merge the pull request to `main` before using `main` as the Pages source.

## Privacy and security
- Tasks stay in this browser's local storage unless exported by the user.
- Do not enter passwords, API keys, health records, or highly sensitive personal data.
- Never commit tokens or credentials. Use repository/environment secrets for future integrations.
- The workflow performs validation only. It does not deploy, message customers, spend money, or modify external accounts.

## Roadmap
1. Add a backend and authenticated user accounts if cloud sync becomes necessary.
2. Add CRM/contact management only with explicit data ownership and access controls.
3. Connect AI providers through a server-side API; never embed provider keys in frontend JavaScript.
4. Add integrations individually, with tests, audit logs, and a documented rollback plan.

## License
MIT. See [LICENSE](LICENSE).
