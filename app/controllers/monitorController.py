from fastapi import HTTPException
from tortoise.contrib.fastapi import register_tortoise
from tortoise.functions import Count
from tortoise import Tortoise
from ..models.ticketModel import Ticket
from ..models.ticketLogModel import Ticketlog
from ..models.autorizathionRequestModel import Autorizathion_request
from ..models.ticketCommentModel import Ticketcomment
import random
from uuid import UUID

# Functions that interact with the ORM
async def getAlert(instalacion_id: UUID):
    try:
        #ticket = await Ticket.get()

        #query = Ticket.filter(instalacion_id=instalacion_id).annotate(group_count=Count('groups')).order_by('goup_count')
        data = await Ticket.filter(instalacion_id=instalacion_id).annotate(count=Count('instalacion_id')).group_by("groups").order_by('count').values("groups", "count")

        # Una instalacion puede tener varias alertas rojas y amarillas a la vez? C y D
        # Cual es el campo que me indica si la alerta esta activa
        # Los ticket estan asociados a un evento que lo gatilló
        # Necesito datos de prueba

        buffer = {}
        for detail in data:
            buffer[detail['groups']] = int(detail['count'])

        if 'A' in buffer.keys() and buffer['A'] > 0:
            alert = 1
        elif 'B' in buffer.keys() and buffer['B'] > 0:
            alert = 2
        elif 'C' in buffer.keys() and buffer['C'] > 0:
            alert = 3
        else:
            alert = 0

        list_response = [0, 1, 2, 3]
        alert = random.choice(list_response)

        history = [{
            'fecha': '12/04/2023',
            'evento': 'Terremoto perceptible en que el operador no puede mantenerse de pie.',
            'alerta': 'Amarilla',
            'estado': 'Cerrada',
            'descripcion': 'Se detecta un sismo que genera un movimiento suficientemente fuerte para que un operador no pueda continuar en pie. Su activación puede ser manual o automática, a través de un acelerógrafo.',
            'mensaje': 'La evaluación de la situación indica que no hay peligro de inestabilidad y la alerta se puede cerrar.'
        },{
            'fecha': '14/05/2023',
            'evento': 'Terremoto perceptible en que el operador no puede mantenerse de pie.',
            'alerta': 'Amarilla',
            'estado': 'Abierta',
            'descripcion': 'Se detecta un sismo que genera un movimiento suficientemente fuerte para que un operador no pueda continuar en pie. Su activación puede ser manual o automática, a través de un acelerógrafo.',
            'mensaje': 'La autoridad y la compañía minera están evaluando la situación. Se informará a la brevedad.'
        },{
            'fecha': '15/06/2023',
            'evento': 'Terremoto perceptible en que el operador no puede mantenerse de pie.',
            'alerta': 'Amarilla',
            'estado': 'Cerrada',
            'descripcion': 'Se detecta un sismo que genera un movimiento suficientemente fuerte para que un operador no pueda continuar en pie. Su activación puede ser manual o automática, a través de un acelerógrafo.',
            'mensaje': 'La evaluación de la situación indica que no hay peligro de inestabilidad y la alerta se puede cerrar.',
        },{
            'fecha': '18/06/2023',
            'evento': 'Terremoto perceptible en que el operador no puede mantenerse de pie.',
            'alerta': 'Amarilla',
            'estado': 'Abierta',
            'descripcion': 'Se detecta un sismo que genera un movimiento suficientemente fuerte para que un operador no pueda continuar en pie. Su activación puede ser manual o automática, a través de un acelerógrafo.',
            'mensaje': 'La autoridad y la compañía minera están evaluando la situación. Se informará a la brevedad.',
        }]

        return { "status": 200, "response": { "alert": alert, "history": history } }

    except Exception as e:
        return { "status": 500 }

# Functions that interact with the ORM
"""
async def getHistoryAlert(instalacion_id: UUID):
    try:
        buffer = [{
            'fecha': '12/04/2023',
            'evento': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'alerta': 'Verde',
            'estado': 'Activo',
            'descripcion': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'mensaje': 'Lorem ipsum dolor sit amet consectetur pellentesque'
        },{
            'fecha': '14/05/2023',
            'evento': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'alerta': 'Amarilla',
            'estado': 'Inactivo',
            'descripcion': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'mensaje': 'Lorem ipsum dolor sit amet consectetur pellentesque'
        },{
            'fecha': '15/06/2023',
            'evento': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'alerta': 'Roja',
            'estado': 'Inactivo',
            'descripcion': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'mensaje': 'Lorem ipsum dolor sit amet consectetur pellentesque'
        }]

        return { "status": 200, "response": buffer }

    except Exception as e:
        return { "status": 500 }
"""