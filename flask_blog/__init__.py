import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '2c6f7da15b2e9db5e91dd289c8e75a9f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Set up login manager to enforce login required for some routes
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' # tells login manager where to login
login_manager.login_message_category = 'info'

# Configure email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASS")

# Email debug (remove these lines when fixed)
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False

# Keep this
mail = Mail(app)

# import & register blueprints
from flask_blog.users.routes import users 
from flask_blog.posts.routes import posts 
from flask_blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
