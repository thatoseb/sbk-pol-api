from marshmallow import post_load, fields

from ma import ma
from model.case import Case
from schema.user import UserSchema


class CaseSchema(ma.Schema):
    date = fields.Str()
    location = fields.Str()
    created_by = fields.Nested(UserSchema)

    @post_load
    def make_case(self, data, **kwargs):
        return Case(**data)
