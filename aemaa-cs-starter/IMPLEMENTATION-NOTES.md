# Implementation Notes

## Before calling this production-ready
- Generate the full project with the current Adobe AEM Project Archetype.
- Confirm Java and AEM SDK compatibility for the target Cloud Manager program.
- Add the required Maven dependencies for Sling Models, AEM APIs, JUnit 5 and AEM Mocks in the generated core module.
- Confirm HTL component resource type, component registration and package filters.
- Integrate the component into an allowed editable template and policy.
- Validate Dispatcher configuration with the matching Dispatcher Tools; the sample farm is illustrative, not a complete farm.
- Configure Cloud Manager pipeline and environment-specific settings in Adobe.
- Add integration/UI tests, accessibility checks, dependency scanning and performance budgets.
- Use persisted GraphQL queries and the target environment's approved authentication/CORS strategy for production.

## Scope of the examples
The Sling Model and HTL demonstrate an authorable component pattern. The TypeScript helper demonstrates safe response/error handling for GraphQL. No credentials, production endpoints or Adobe environment IDs are included.
