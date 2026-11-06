# AEM as a Cloud Service Starter

This folder contains starter examples and implementation notes for an AEMaaCS project. It is intentionally a **starter kit**, not a complete production deployment package.

## Recommended project generation

Generate the full Maven project using the current Adobe AEM Project Archetype. Use the archetype version and SDK compatibility documented by Adobe for your target Cloud Manager program.

```bash
mvn -B org.apache.maven.plugins:maven-archetype-plugin:3.3.1:generate \
  -DarchetypeGroupId=com.adobe.aem \
  -DarchetypeArtifactId=aem-project-archetype \
  -DarchetypeVersion=<CURRENT_ARCHETYPE_VERSION> \
  -DappTitle="AEM Cloud Starter" \
  -DappId="aemcloudstarter" \
  -DgroupId="com.fashionlooks" \
  -DartifactId="aem-cloud-starter" \
  -Dpackage="com.fashionlooks.aemcloudstarter" \
  -DfrontendModule="general"
```

Replace the placeholder archetype version with the current Adobe-supported version. Review generated modules and merge the examples below into the generated structure.

## Included examples

- `core/`: Sling Model example and unit test pattern.
- `ui.apps/`: HTL component and author dialog example.
- `frontend/`: TypeScript GraphQL client example.
- `dispatcher/`: illustrative Dispatcher filter example.

## Build and validate

Run Maven from the generated project root:

```bash
mvn clean verify
```

Use the AEM SDK and Dispatcher Tools matching your target AEMaaCS program. The examples here are not a substitute for validating against that SDK.

## Security notes

- Never commit credentials, access tokens, production content or private keys.
- Use service users with least privilege.
- Validate and encode user input.
- Restrict Dispatcher paths and methods; review filters with the security team.
- Use approved secret management for external integrations.
