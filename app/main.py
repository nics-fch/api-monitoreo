from fastapi import FastAPI

from .api.v1.api import api 

app = FastAPI(
    title="API BASE",
    description="Api base para proyectos",
    version="1.0.0",
    )


# API Versioning
app.include_router(api, prefix="/api/v1")


