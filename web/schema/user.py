from marshmallow import post_load, fields

from ma import ma
from model.user import User


class UserSchema(ma.Schema):
    username = fields.Str()
    password = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    country_origin = fields.Str()
    identification_num = fields.Str()
    email = fields.Str()

    class Meta:
        load_only = ('password',)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
