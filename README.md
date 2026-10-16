# HN Tech Radar

Daily Hacker News intelligence research covering AI, cybersecurity, AWS/cloud, DevOps, and emerging technology.

## Repository structure

- `data/hn-tech-radar/latest.json` — latest report
- `data/hn-tech-radar/archive/` — dated archive of previous reports
- `scripts/publish-hn-tech-radar.ps1` — PowerShell publish script

## Publishing

Run the publish script from the repo root:

```
powershell -ExecutionPolicy Bypass -File scripts/publish-hn-tech-radar.ps1
```

The script validates the report, archives the previous version, commits, and pushes to `origin/master`.

## Live site

`https://jazblue.github.io/tech-hn-radar/`