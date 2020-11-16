import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    # Configure email
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get("EMAIL_USER")
    MAIL_PASSWORD = config.get("EMAIL_PASS")

