from tortoise.models import Model
from tortoise import fields

class Tranque(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    status = fields.BooleanField()