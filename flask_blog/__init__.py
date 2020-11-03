from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2c6f7da15b2e9db5e91dd289c8e75a9f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Set up login manager to enforce login required for some routes
login_manager = LoginManager(app)
login_manager.login_view = 'login' # tells login manager where to login
login_manager.login_message_category = 'login'

# import routes after creating the app variable to avoid circular import
from flask_blog import routes
