from tortoise.models import Model
from tortoise import fields

class Ticket(Model):
    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(null=True)
    updated_at = fields.DatetimeField(null=True)
    module = fields.CharField(null=True, max_length=510)
    state = fields.CharField(null=True, max_length=510)
    result_state = fields.JSONField(null=True)
    spread_object = fields.JSONField(null=True)
    archived = fields.BooleanField(null=True)
    close_conditions = fields.JSONField(null=True)
    evaluable = fields.BooleanField(null=True)
    groups =fields.CharField(null=True, max_length=510)
    archive_conditions = fields.JSONField(null=True)
    escalate_conditions = fields.JSONField(null=True)
    origin = fields.CharField(null=True, max_length=255)
    propagated = fields.BooleanField(null=True)
    ticket_display = fields.CharField(null=True, max_length=30)
    instalacion_id = fields.UUIDField()