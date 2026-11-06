# Security, Performance, SEO and Accessibility

## Security
- Use least-privilege service users and permissions.
- Validate and encode untrusted input; avoid injection-prone query construction.
- Store secrets in approved secret stores and rotate them.
- Configure Dispatcher filters to deny unintended paths and methods.
- Review CORS, CSP, cache headers, authentication and authorization.
- Scan dependencies and remediate vulnerabilities.
- Never log access tokens, credentials, personal data or sensitive payloads.

## Performance
- Prefer cacheable publish responses and correct cache keys.
- Keep client libraries lean; minimize JavaScript and CSS.
- Optimize images and responsive renditions.
- Avoid expensive repository queries; use appropriate Oak indexes.
- Measure server response, frontend rendering and real-user metrics.
- Set performance budgets and observe Core Web Vitals.

## SEO
- Provide unique titles, descriptions and canonical URLs.
- Maintain redirects during migrations.
- Generate valid sitemap and robots directives for the target environment.
- Use semantic HTML and structured data where appropriate.
- Ensure important content is crawlable and internal links are healthy.

## Accessibility
- Use semantic landmarks and logical heading order.
- Ensure keyboard access and visible focus.
- Provide labels and meaningful alternative text.
- Check contrast and zoom/reflow behavior.
- Combine automated tools with manual assistive-technology checks.
