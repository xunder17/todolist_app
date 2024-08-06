from flask import Flask
from flask_restful import Api
from app.models import db
from app.resources.user import UserListResource, UserResource
from app.resources.task import TaskListResource, TaskResource


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<int:user_id>')
    api.add_resource(TaskListResource, '/tasks')
    api.add_resource(TaskResource, '/tasks/<int:task_id>')

    with app.app_context():
        db.create_all()

    return app
