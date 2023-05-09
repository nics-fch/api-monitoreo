# Desarrollo local

- Levantar con docker-compose up -d --build
- localhost:8085/docs

## Docker build and push

```bash
docker login registry.gitlab.com

docker build -t registry.gitlab.com/trq-fundacion/api-monitoreo:infy-dev .
docker push registry.gitlab.com/trq-fundacion/api-monitoreo:infy-dev
```