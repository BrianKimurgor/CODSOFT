from the_app import db
from flask_login import UserMixin

"""
defining UserMixin to implement:
- is_active
- is_authenticated
- get_id()
"""
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)


    def __repr__(self):
        return f'User{self.first_name}{self.email}'



"""
create task model
each user can have many todos
create one to many relationships between User and Task model
"""

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(255))
    due_date = db.Column(db.DateTime())
    status = db.Column(db.String(255))
    todo_owner = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f'Task{self.task_name}{self.due_date}'
