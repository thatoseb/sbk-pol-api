from flask import Flask
from flask_restful import Api


from db import db
from ma import ma
from resources.user.user import UserResource, UserRegisterResource
from resources.case.case import CaseResource, CasesResource

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'mymongodb'
app.config['MONGOALCHEMY_SERVER'] = 'db'
app.config['MONGOALCHEMY_PORT'] = '27017'
api = Api(app)

api.add_resource(UserResource, '/api/user/<string:username>')
api.add_resource(UserRegisterResource, '/api/user/register')
api.add_resource(CaseResource, '/api/case/<string:username>')
api.add_resource(CasesResource, '/api/cases')


db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)