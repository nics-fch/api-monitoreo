from fastapi import APIRouter

target_router = APIRouter()


@target_router.get("/")
async def root():
    return {"message": "Hello carla"}
