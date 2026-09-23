# Security

Do not commit passwords, API keys, access tokens, database credentials, SMTP credentials, private certificates, or other secrets.

Use environment variables for local configuration and provide a safe `.env.example` when configuration needs to be documented.

If a secret is accidentally committed, rotate or revoke it immediately and then remove it from the repository and, when necessary, its Git history.
