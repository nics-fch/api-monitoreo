from fastapi import APIRouter, HTTPException, Depends
#from tortoise.contrib.fastapi import register_tortoise
#from tortoise.exceptions import DoesNotExist
from ..controllers.monitorController import getAlert, getHistoryAlert
from uuid import UUID

# We create our router
router = APIRouter()

# Route list
@router.get("/getAlert/{instalacion_id}", response_model=None)
async def getAlertRoute(instalacion_id: UUID):
    data = await getAlert( instalacion_id )
    """
    if listRegiones is None:
        raise HTTPException(status_code=404, detail="Deposito not found")
    """
    return data

@router.get("/getHistoryAlert/{instalacion_id}", response_model=None)
async def getHistoryAlertRoute(instalacion_id: UUID):
    data = await getHistoryAlert( instalacion_id )
    """
    if listRegiones is None:
        raise HTTPException(status_code=404, detail="Deposito not found")
    """
    return data