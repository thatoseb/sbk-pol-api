from flask_restful import Resource
from flask import request

from model.case import Case
from model.user import User
from schema.case import CaseSchema

case_schema = CaseSchema()


CREATED_SUCCESSFULLY = 'Case successfully created'
USER_NOT_REGISTERED = 'User, with username {}, is not a registered user'


class CaseResource(Resource):

    @classmethod
    def post(cls, username: str):
        case_json = request.get_json()
        case = case_schema.load(case_json)
        user = User.find_by_username(username)

        if user:
            case.created_by = user
            case.save_case()
        else:
            return {'message': USER_NOT_REGISTERED.format(username)}, 404

        return {'message': CREATED_SUCCESSFULLY}, 200

    @classmethod
    def get(cls, username: str):
        user = User.find_by_username(username)

        if user:
            case = Case.find_case_by_user(user)
            return case_schema.dump(case, many=True), 200
        else:
            return {'message': USER_NOT_REGISTERED.format(username)}, 404


class CasesResource(Resource):

    @classmethod
    def get(cls):
        return {'cases': case_schema.dump(Case.find_all(), many=True)}, 200
