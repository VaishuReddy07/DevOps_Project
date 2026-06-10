# Submission guide: commands and screenshots

This file lists exact commands to run and which screenshots to capture for your assignment submission.

## Commands to run (copy/paste)

1) Build image

```bash
cd c:\Users\Vaishnavi\Downloads\DevOps\DevOps
docker build -t myapp .
```

2) Start services

```bash
docker compose up -d
```

3) List running containers

```bash
docker ps
```

4) List images

```bash
docker images
```

5) View Flask logs

```bash
docker logs mysite --tail 50
```

6) Check networks

```bash
docker network ls
```

7) Test endpoints

```bash
curl http://localhost:8000/
curl http://localhost:8000/mysql-time
```

8) Stop and remove

```bash
docker compose down -v
```

## Expected outputs (capture these)

- `docker build` completes successfully (capture terminal output)
- `docker compose up -d` reporting services started
- `docker ps` showing `mysite` and `mysql-container`
- `docker images` showing `myapp`
- `docker logs mysite` showing Flask started and `/mysql-time` requests
- `docker network ls` showing `mynetwork`
- `curl http://localhost:8000/mysql-time` returning JSON with `mysql_time`
- Project tree showing final folder structure

## Screenshots to capture (filenames)

- `build-success.png` — terminal showing `docker build -t myapp .` success
- `compose-up.png` — `docker compose up -d` success
- `docker-ps.png` — `docker ps` output
- `docker-images.png` — `docker images` output
- `docker-logs-mysite.png` — `docker logs mysite --tail 50`
- `network-ls.png` — `docker network ls`
- `mysql-time.png` — `curl` output for `/mysql-time`
- `project-structure.png` — file explorer or `tree` output

## Optional additional captures

- `docker-history-myapp.png` — `docker history myapp`
- `docker-inspect-mysite.png` — `docker inspect mysite`

## Checklist for viva/demo

- [ ] Show `docker build -t myapp .` (build success)
- [ ] Show `docker compose up -d` (services running)
- [ ] Show `docker ps` (containers and ports)
- [ ] Show `curl` to homepage and `/mysql-time`
- [ ] Show `docker logs mysite`
- [ ] Show `docker images` and `docker history myapp`
- [ ] Explain `docker-compose.yml` lines (be ready to walk through file)
- [ ] Explain how Docker networking allows `mysql-container` host resolution

## Notes

- If host port `3306` is already in use, the compose file maps MySQL to host `3307:3306`. Adjust screenshots accordingly.
- Include timestamps on screenshots if possible.

Good luck with your submission.
