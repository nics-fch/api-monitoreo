from fastapi import APIRouter
from .routes.targets import target_router


api = APIRouter()

api.include_router(target_router, prefix="/targets", tags=["targets"])


