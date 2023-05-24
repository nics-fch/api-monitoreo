from tortoise.models import Model
from tortoise import fields

class Autorizathion_request(Model):
    id = fields.UUIDField(pk=True)
    autorizathion = fields.CharField(null=True, max_length=512)
    created_by = fields.JSONField(null=True)
    created_at = fields.DatetimeField(null=True)
    origin = fields.CharField(null=True, max_length=255)
    resolved_by = fields.JSONField(null=True)
    resolved_at = fields.DatetimeField(null=True)
    comment = fields.TextField(null=True)
    status = fields.CharField(null=True, max_length=20)
    received_at = fields.DatetimeField(null=True)
    approval_flag = fields.BooleanField(null=True)
    pendding_flag = fields.BooleanField(null=True)
    ticket = fields.ForeignKeyField('models.Ticket', to_field='id')