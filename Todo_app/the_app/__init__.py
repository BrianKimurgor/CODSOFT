# Importing the necessary dependencies
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# Setting a secret key for Flask (used for session management)
SECRET_KEY = "secret"


# Configuring the Flask application with a secret key and database URI
app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a SQLAlchemy database instance tied to the Flask application
db = SQLAlchemy(app)

from the_app.api.views import todo
app.register_blueprint(todo)


# Creating the database tables with the defined models
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


from the_app.api.models import User
@login_manager.user_loader
def load_user(user_id):
    from the_app.api.models import User
    return User.query.get(int(user_id))
