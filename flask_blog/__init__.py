from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config) # takes configurations from config.py

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Set up login manager to enforce login required for some routes
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' # tells login manager where to login
login_manager.login_message_category = 'info'



mail = Mail(app)

# import & register blueprints
from flask_blog.users.routes import users 
from flask_blog.posts.routes import posts 
from flask_blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
