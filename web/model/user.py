from typing import List

from db import db


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    country_origin = db.StringField(required=True)
    identification_num = db.StringField(required=True)
    email = db.StringField(required=True)

    @classmethod
    def find_all(cls) -> List['User']:
        return cls.query.all()

    @classmethod
    def find_by_username(cls, username: str) -> 'User':
        return cls.query.filter(cls.username == username).first()

    @classmethod
    def find_by_identification_num(cls, identification_num: str) -> 'User':
        return cls.query.filter(cls.identification_num == identification_num).first()

    def save_user(self) -> None:
        db.session.save(self)






