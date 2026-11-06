# AEMaaCS Learning & Delivery Roadmap

## Phase 1 — Java and platform foundations
- [ ] Core Java: collections, streams, generics, exceptions, concurrency and JVM basics.
- [ ] Understand Java 11/17/21 compatibility with the selected AEM SDK/runtime; do not assume every version is interchangeable.
- [ ] Maven lifecycle, dependency management and multi-module builds.
- [ ] OSGi bundles, services, configurations and lifecycle.
- [ ] Apache Sling: resource resolution, request processing, servlets, filters and resource types.
- [ ] JCR nodes/properties, queries, Oak indexes and repository constraints.
**Deliverable:** a small Sling service and servlet module with unit tests.

## Phase 2 — AEM application development
- [ ] Generate a project using the current Adobe AEM Project Archetype.
- [ ] Understand core, ui.apps, ui.content, ui.config, all and dispatcher modules.
- [ ] Build Sling Models and exporters where required.
- [ ] Use Core Components and proxy components.
- [ ] Create Editable Templates, policies, dialogs, components and client libraries.
- [ ] Build responsive HTL and authoring-friendly components.
- [ ] Implement Content Fragment and Experience Fragment use cases.
**Deliverable:** a responsive authorable site with reusable components.

## Phase 3 — Cloud-native AEM operations
- [ ] Understand AEMaaCS author, publish, preview (where enabled) and asset processing architecture.
- [ ] Configure Dispatcher filters, caching, rewrites and security headers.
- [ ] Understand immutable/reproducible deployments and run modes.
- [ ] Configure Cloud Manager pipelines, quality gates, variables and secrets.
- [ ] Use Adobe-supported local SDK tooling; local SDK is not identical to cloud runtime.
**Deliverable:** code and dispatcher configuration prepared for Cloud Manager.

## Phase 4 — Integrations and headless
- [ ] Consume REST APIs with timeouts, retries and safe secret handling.
- [ ] Design Content Fragment Models and GraphQL queries.
- [ ] Build a React/TypeScript client using GraphQL or persisted queries.
- [ ] Define CORS, authentication, caching and API error behavior.
**Deliverable:** a small headless content experience with documented API contracts.

## Phase 5 — Migration from AMS / on-premise
- [ ] Inventory content, assets, components, templates, workflows, users, integrations and custom code.
- [ ] Identify unsupported APIs, legacy patterns and repository assumptions.
- [ ] Map assets, metadata, tags, redirects and URL behavior.
- [ ] Plan content transfer, delta migration, validation and rollback.
- [ ] Rebuild dispatcher and deployment processes for Cloud Manager.
- [ ] Execute performance, authoring, security and acceptance tests.
**Deliverable:** migration assessment, cutover plan and reconciliation checklist.

## Phase 6 — Quality and operations
- [ ] Unit tests with JUnit and AEM Mocks where appropriate.
- [ ] Static analysis, dependency scanning and code quality checks.
- [ ] Integration and UI automation.
- [ ] Accessibility: keyboard, semantic structure, contrast and labels.
- [ ] SEO: metadata, canonical URLs, structured data and sitemap.
- [ ] Core Web Vitals, monitoring, logging, alerting and runbooks.
**Deliverable:** release checklist and operational runbook.

## Phase 7 — Advanced / optional
- [ ] Adobe Target, Analytics and AEP.
- [ ] Marketo and Journey Optimizer.
- [ ] App Builder and Firefly extensibility.
- [ ] Edge Delivery Services.
- [ ] AEM Forms and Assets Content Hub.
- [ ] Adobe certifications relevant to target role.

Track every task with evidence: pull request, test output, architecture note, demo or deployment record.
