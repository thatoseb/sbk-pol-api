from typing import List

from db import db


class Task(db.Document):
    id = db.IntField()
    title = db.StringField()
    description = db.StringField()
    done = db.BoolField()

    @classmethod
    def find_all(cls) -> List["Task"]:
        return cls.query.all()
