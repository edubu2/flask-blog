from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2c6f7da15b2e9db5e91dd289c8e75a9f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# import routes after creating the app variable to avoid circular import
from flask_blog import routes
