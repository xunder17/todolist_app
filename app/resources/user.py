from flask import request
from flask_restful import Resource
from app.models import db, User
from app.schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users), 200

    def post(self):
        data = request.get_json()
        errors = user_schema.validate(data)
        if errors:
            return errors, 400

        new_user = User(
            username=data['username'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user), 200

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        errors = user_schema.validate(data)
        if errors:
            return errors, 400

        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return user_schema.dump(user), 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204
