# AEMaaCS Reference Architecture

## Request and content flow
1. Authors create content using editable templates, components, Content Fragments and Assets.
2. Content is activated and delivered through AEM publish; preview may be used where configured.
3. Dispatcher / CDN caching and filtering protect and accelerate delivery.
4. Headless clients may consume Content Fragment GraphQL APIs or persisted queries, subject to the selected security model.
5. External systems integrate through controlled REST APIs or Adobe extensibility services.

## Typical Maven project modules
- **core:** Java code — Sling Models, OSGi services, servlets, schedulers and tests.
- **ui.apps:** component definitions, dialogs, client libraries, HTL and application configuration.
- **ui.content:** deployable content and structure such as templates, policies and sample content.
- **ui.config:** OSGi configuration organized by run mode.
- **all:** aggregate package used to assemble deployment artifacts.
- **dispatcher:** Apache HTTPD / Dispatcher configuration.

Exact modules vary by archetype version and project requirements. Follow the generated project and current Adobe guidance.

## Design principles
- Prefer Core Components and supported extension points.
- Keep authoring configuration separate from Java implementation.
- Use Sling Models for presentation logic and services for business logic.
- Externalize environment-specific values and secrets.
- Avoid repository writes incompatible with AEMaaCS.
- Design APIs for least privilege, caching, observability and failure handling.
- Treat cloud runtime constraints as architectural requirements.
