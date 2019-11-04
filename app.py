from flask import Flask
from flask_restful import Resource, Api


from db import db
from ma import ma
from model.task import Task
from resources.user.user import UserResource, UserRegisterResource
from resources.case.case import CaseResource, CasesResource
from schema.task import TaskSchema

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'mymongodb'
tasks_collection = TaskSchema(many=True)
api = Api(app)


class TaskResource(Resource):
    @classmethod
    def get(cls):
        return {'tasks': tasks_collection.dump(Task.find_all())}, 200


api.add_resource(TaskResource, '/api/task')
api.add_resource(UserResource, '/api/user/<string:username>')
api.add_resource(UserRegisterResource, '/api/user/register')
api.add_resource(CaseResource, '/api/case/<string:username>')
api.add_resource(CasesResource, '/api/cases')


db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)