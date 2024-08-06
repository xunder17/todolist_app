from flask import request
from flask_restful import Resource
from app.models import db, Task
from app.schemas import TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


class TaskListResource(Resource):
    def get(self):
        status = request.args.get('status')
        if status:
            tasks = Task.query.filter_by(status=status).all()
        else:
            tasks = Task.query.all()
        return tasks_schema.dump(tasks), 200

    def post(self):
        data = request.get_json()
        errors = task_schema.validate(data)
        if errors:
            return errors, 400

        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', 'pending'),
            user_id=data['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task), 201


class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return task_schema.dump(task), 200

    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        errors = task_schema.validate(data)
        if errors:
            return errors, 400

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        db.session.commit()
        return task_schema.dump(task), 200

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204
