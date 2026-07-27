# Security policy

## Supported code

Security fixes target the source files listed in `manifest.json`. Deprecated or locally modified copies are not supported.

## Reporting a vulnerability

Use a private GitHub Security Advisory for the repository when available. Do not publish credentials, webhook URLs, private alert payloads or exploitable account details in a public issue.

Include the affected script/version, impact, reproduction steps and any safe proof of concept.

## Security boundaries

Meridian Pine scripts do not store credentials, make arbitrary network requests or directly connect to brokers, Discord or other external services. TradingView alerts can transmit data only after a user creates an alert and configures a destination.

Users are responsible for protecting webhook URLs, API gateways and downstream automation. Never place a secret in public Pine source or a reusable alert template.
