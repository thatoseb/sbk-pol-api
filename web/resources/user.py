from flask_restful import Resource
from flask import request

from model.user import User
from schema.user import UserSchema

USER_NOT_FOUND = 'User, {} NOT FOUND'
USER_ALREADY_EXISTS = 'User with {}, {} has already been registered'
CREATED_SUCCESSFULLY = "User created successfully."

user_schema = UserSchema()


class UserResource(Resource):

    @classmethod
    def get(cls, username: str):
        user = User.find_by_username(username)
        if user:
            return user_schema.dump(user), 200
        return {'message': USER_NOT_FOUND.format(username)}, 404


class UserRegisterResource(Resource):

    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if User.find_by_username(user.username):
            return {'message': USER_ALREADY_EXISTS.format('username', user.username)}, 400

        if User.find_by_identification_num(user.identification_num):
            return {'message': USER_ALREADY_EXISTS.format('identification number', user.identification_num)}, 400

        user.save_user()

        return {'message': CREATED_SUCCESSFULLY}, 200

