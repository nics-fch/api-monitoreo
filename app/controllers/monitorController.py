from fastapi import HTTPException
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from ..models.tranqueModel import Tranque

# Functions that interact with the ORM
async def getStatus(tranque_id: int):
    try:
        return await Tranque.get(id=tranque_id)
    except Exception as e:
        return {}