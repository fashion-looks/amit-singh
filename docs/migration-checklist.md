# AEM Migration Checklist — AMS / On-Premise to AEMaaCS

## Discover
- [ ] Source versions, topology, integrations and operational ownership recorded.
- [ ] Content volume, assets, language copies, tags and users inventoried.
- [ ] Custom components, templates, workflows, services and scheduled jobs catalogued.
- [ ] External integrations and authentication dependencies documented.
- [ ] Dispatcher rules, rewrites, redirects, headers and cache behavior captured.

## Assess and remediate
- [ ] Run Adobe-recommended code and repository assessments.
- [ ] Identify deprecated APIs and unsupported implementation patterns.
- [ ] Remove reliance on mutable application binaries or local filesystem state.
- [ ] Review Oak queries and indexes for performance and compatibility.
- [ ] Review OSGi configs and run-mode assumptions.
- [ ] Validate workflows, asset processing and content policies.
- [ ] Rework dispatcher configuration to current supported patterns.

## Plan and execute
- [ ] Define Cloud Manager program, environments and pipeline strategy.
- [ ] Define content migration approach and ownership.
- [ ] Perform rehearsal migration and capture timings.
- [ ] Validate content counts, references, renditions, permissions and URLs.
- [ ] Plan delta migration and content freeze windows.
- [ ] Create rollback and recovery decision criteria.

## Validate and launch
- [ ] Functional author and publish smoke tests passed.
- [ ] SEO, redirects, analytics and consent behavior validated.
- [ ] Security and accessibility checks passed.
- [ ] Load, cache and Core Web Vitals targets met.
- [ ] Business owner sign-off completed.
- [ ] Cutover communications and support rota published.
- [ ] Post-launch reconciliation and monitoring completed.
