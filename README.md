# DevOps - FlaskWebProject1

This repository contains a containerized Flask application and MySQL (assignment).

## What is included

- Flask app: `FlaskWebProject1/` (`__init__.py`, `views.py`, `templates/`, `static/`)
- `runserver.py` — development entrypoint
- `Dockerfile` — builds the Flask image from `python:3.9-slim`
- `requirements.txt` — Python dependencies (includes `mysql-connector-python`)
- `docker-compose.yml` — starts Flask and MySQL with a named volume and custom network
- `.dockerignore`

## Quick start (local)

1. Build image:

bash
cd c:\Users\Vaishnavi\Downloads\DevOps\DevOps
docker build -t myapp .

2. Start services with Compose:

bash
docker compose up -d

3. Verify endpoints:

bash
curl http://localhost:8000/
curl http://localhost:8000/mysql-time

Expected `/mysql-time` response:

json
{"mysql_time":"2026-06-06T18:58:43"}

4. Stop and remove:

bash
docker compose down -v

## Rebuild after code changes

- Rebuild image:
bash
docker build -t myapp .

- Or rebuild via Compose:

bash
docker compose build mysite
docker compose up -d

## Troubleshooting (common issues)

- Dockerfile not found: ensure you are in the project root and `Dockerfile` exists; run `docker build -f Dockerfile .`
- Port already in use: use `netstat -ano | findstr ":8000"` (Windows) or change host mapping `-p 8001:8000`.
- Container exited immediately: inspect `docker logs <container>` and `docker ps -a`.
- MySQL connection refused: ensure both containers share the same user-defined network and use service name `mysql-container` as host; check `docker logs mysql-container` for readiness.

## Project structure (final)

DevOps/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── main.tf
├── requirements.txt
├── runserver.py
└── FlaskWebProject1/
    ├── __init__.py
    ├── views.py
    ├── static/
    └── templates/

## Azure VM deployment (summary)

1. Copy project to VM (scp / az cli)
2. Install Docker on VM (official instructions)
3. Pull or build image on VM
4. Run container or `docker compose up -d`
5. Open inbound port 8000 in Azure NSG
6. Verify with `http://<VM_PUBLIC_IP>:8000/`

---

For submission artifacts and required screenshots, see `SUBMISSION.md`.
