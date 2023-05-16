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
            group = 1
        elif 'B' in buffer.keys() and buffer['B'] > 0:
            group = 2
        elif 'C' in buffer.keys() and buffer['C'] > 0:
            group = 3
        else:
            group = 0

        list_response = [0, 1, 2, 3]
        v = random.choice(list_response)

        return { "status": 200, "response": v }

    except Exception as e:
        return { "status": 500 }

# Functions that interact with the ORM
async def getHistoryAlert(instalacion_id: UUID):
    try:
        """
        data = await Ticket.filter(
            # Filtros opcionales para ModelA
        ).prefetch_related(
            'related_model_b',
            'related_model_b__related_model_c',
            'related_model_d'
        )
        """

        #tickets = Ticket.filter(instalacion_id=instalacion_id)

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