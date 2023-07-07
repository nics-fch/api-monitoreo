from fastapi import HTTPException
from tortoise.contrib.fastapi import register_tortoise
from tortoise.functions import Count
from tortoise import Tortoise
from ..models.monitorModel import Semaforo, Historial_alertas
import random
from uuid import UUID

# Functions that interact with the ORM
async def getAlert(instalacion_id: UUID):
    try:
        data = await Semaforo.get_or_none(instalacion_id=instalacion_id)

        alert = 1
        if data:
            if data.color_alerta.lower() == 'verde':
                alert = 1
            elif data.color_alerta.lower() == 'amarilla':
                alert = 2
            elif data.color_alerta.lower() == 'roja':
                alert = 3

        history = []
        data_history = await Historial_alertas.filter(instalacion_id=instalacion_id)

        for detail in data_history:
            buffer = dict(detail)
            buffer["fecha"] = buffer["fecha"].strftime("%d/%m/%Y %H:%M:%S")
            history.append(buffer)

        return { "status": 200, "response": { "alert": alert, "history": history } }

    except Exception as e:
        return { "status": 500 }