import os

class Config:
    SECRET_KEY = os.environ.get("FB_SECRET")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")
    # Configure email
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASS")