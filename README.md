# Desarrollo local

```bash
docker-compose up -d --build
```

localhost:8086/docs

## Docker build and push

```bash
docker login registry.gitlab.com

docker build -t registry.gitlab.com/trq-fundacion/api-monitoreo:tagname .
docker push registry.gitlab.com/trq-fundacion/api-monitoreo:tagname
```