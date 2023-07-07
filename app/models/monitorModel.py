from tortoise.models import Model
from tortoise import fields

class Semaforo(Model):
    instalacion_id = fields.UUIDField(pk=True)
    conectado = fields.BooleanField(null=True)
    color_alerta = fields.CharField(null=True, max_length=10)
    descripcion = fields.CharField(null=True, max_length=510)
    observaciones = fields.CharField(null=True, max_length=510)

class Historial_alertas(Model):
    id = fields.UUIDField(pk=True)
    instalacion = fields.ForeignKeyField('models.Semaforo', to_field='instalacion_id', column_name='instalacion_id')
    fecha = fields.DatetimeField(null=True)
    evento = fields.CharField(null=True, max_length=25)
    alerta = fields.CharField(null=True, max_length=20)
    estado = fields.CharField(null=True, max_length=20)
    descripcion = fields.CharField(null=True, max_length=1000)
    mensaje = fields.CharField(null=True, max_length=1000)