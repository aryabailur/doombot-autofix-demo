# doombot-autofix-demo

A scenario repository for demoing Doombot's auto-fix draft PRs (F19).

The history here is deliberate:

1. `fetch()` shipped without a default for `timeout`.
2. Someone reported the crash, and it was fixed in a pull request.
3. The fix was later lost, so the same crash came back.
4. Doombot is asked to triage the new report.

Safe to delete.
