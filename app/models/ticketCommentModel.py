from tortoise.models import Model
from tortoise import fields

class Ticketcomment(Model):
    id = fields.UUIDField(pk=True)
    comment_type = fields.CharField(null=True, max_length=25)
    content = fields.TextField(null=True)
    created_by = fields.JSONField(null=True)
    created_at = fields.DatetimeField(null=True)
    origin = fields.CharField(null=True, max_length=255)
    updated_at = fields.DatetimeField(null=True)
    ticket = fields.ForeignKeyField('models.Ticket', to_field='id')