from tortoise.models import Model
from tortoise import fields

class Ticketlog(Model):
    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(null=True)
    highligth = fields.BooleanField(null=True)
    timeseries = fields.JSONField(null=True)
    meta = fields.JSONField(null=True)
    author = fields.JSONField(null=True)
    origin = fields.CharField(null=True, max_length=255)
    ticket = fields.ForeignKeyField('models.Ticket', to_field='id')