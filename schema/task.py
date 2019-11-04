from marshmallow import post_load, fields

from ma import ma
from model.task import Task


class TaskSchema(ma.Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    done = fields.Bool()

    @post_load
    def make_user(self, data, **kwargs):
        return Task(**data)
