# Public Release Checklist

Before pushing this repository publicly:

- [ ] Run all unit tests.
- [ ] Run `python scripts/validate_repository.py`.
- [ ] Confirm `.env`, workbooks, logs, credentials, and local configs are ignored.
- [ ] Search tracked content for internal hostnames, IP addresses, usernames, network paths, tokens, and tenant IDs.
- [ ] Confirm sample data is entirely synthetic.
- [ ] Confirm screenshots and diagrams contain no internal identifiers.
- [ ] Review commit history, not only the current working tree, for removed secrets.
- [ ] Use a GitHub secret-scanning or pre-commit control before publication.
- [ ] Have the appropriate organizational reviewer approve public release.

Never publish a secret and then merely delete it in a later commit; rotate the secret and rewrite history through an approved process.
