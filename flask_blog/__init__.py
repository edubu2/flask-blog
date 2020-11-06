from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_blog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()

# Set up login manager to enforce login required for some routes
login_manager = LoginManager()
login_manager.login_view = 'users.login' # tells login manager where to login
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class) 

    # Initialize extensions from above
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # import & register blueprints
    from flask_blog.users.routes import users
    from flask_blog.posts.routes import posts 
    from flask_blog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
