import os
import json

with open('/etc/config.json') as config_file
	config = json.load(config_file)

class Config:
    SECRET_KEY = config.get("FB_SECRET")
    SQLALCHEMY_DATABASE_URI = config.get("DB_URI")
    # Configure email
    MAIL_SERVER = config.get("MAIL_SERVER")
    MAIL_PORT = config.get("MAIL_PORT")
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get("MAIL_USERNAME")
    MAIL_PASSWORD = config.get("MAIL_PASS")
