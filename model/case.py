from typing import List

from db import db
from model.user import User


class Case(db.Document):
    date = db.StringField(required=True)
    location = db.StringField(required=True)
    created_by = db.DocumentField(User)

    @classmethod
    def find_all(cls) -> List['Case']:
        return cls.query.all()

    @classmethod
    def find_case_by_user(cls, user: User) -> List['Case']:
        user_cases = cls.query.filter(cls.created_by == user).all()
        return user_cases

    def save_case(self) -> None:
        db.session.save(self)
