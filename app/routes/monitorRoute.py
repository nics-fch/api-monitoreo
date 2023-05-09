from fastapi import APIRouter, HTTPException, Depends
#from tortoise.contrib.fastapi import register_tortoise
#from tortoise.exceptions import DoesNotExist
from ..controllers.monitorController import getStatus

# We create our router
router = APIRouter()

# Route list
@router.get("/tranque/{tranque_id}", response_model=None)
async def getStatusRoute(tranque_id: int):
    myTranque = await getStatus(tranque_id)
    if myTranque is None:
        raise HTTPException(status_code=404, detail="Tranque not found")
    return myTranque
