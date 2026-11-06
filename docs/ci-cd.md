# CI/CD and Cloud Manager

## Local development
- Generate the application from the current Adobe AEM Project Archetype.
- Use the AEM SDK and Dispatcher Tools versions appropriate to the target program.
- Build with Maven and run unit tests before pushing.
- Keep local secrets out of source control.

## Pipeline flow
1. Developer creates a branch and pull request.
2. CI checks formatting, Maven compilation, unit tests, static analysis and dependency risks.
3. Review and merge to the configured integration branch.
4. Cloud Manager executes the configured build and quality gates.
5. Deploy to the target environment through the approved pipeline.
6. Run smoke tests and confirm author/publish/dispatcher behavior.
7. Promote to production only with required approvals and release evidence.

## Repository workflow
- Protect the main branch.
- Require pull-request reviews and passing checks.
- Pin GitHub Actions to reviewed versions or full commit SHAs in production.
- Use approved secret storage for non-Adobe cloud integrations.
- Never store Adobe credentials, API keys or production data in Git.

## Important distinction
The GitHub Actions workflow in this repository is generic Maven validation. It does not deploy to AEM Cloud Manager. Configure deployment in Adobe Cloud Manager according to your organization's Adobe setup.
