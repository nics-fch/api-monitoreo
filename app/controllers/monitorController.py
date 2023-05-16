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
            'evento': 'Lorem ipsum dolor sit amet consectetur pellentesque',
            'alerta': 'Amarillo',
            'estado': 'Activo',
            'descripcion': 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet',
            'mensaje': 'Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis'
        },{
            'fecha': '14/05/2023',
            'evento': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium',
            'alerta': 'Amarilla',
            'estado': 'Inactivo',
            'descripcion': 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque',
            'mensaje': 'Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur'
        },{
            'fecha': '15/06/2023',
            'evento': 'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit',
            'alerta': 'Roja',
            'estado': 'Inactivo',
            'descripcion': 'Aquas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga',
            'mensaje': 'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus.'
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