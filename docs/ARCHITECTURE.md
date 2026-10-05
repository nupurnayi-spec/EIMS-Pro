# EIMS Pro Architecture

1. Presentation: Jinja templates, CSS, JavaScript
2. Application: Flask routes in `app.py`
3. Monitoring: `monitoring/collector.py` and `monitoring/alerts.py`
4. Persistence: SQLite through `utils/db.py`
5. Reporting: `utils/reports.py`

Future enterprise upgrades: RBAC, PostgreSQL, Redis/Celery, WebSockets, remote collection agents, audit logs, Docker and GitHub Actions.
