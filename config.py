import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "You-will-never-guess"
    MAIL_SERVER = os.environ.get("MAIL_SERVER","stmp.googlemail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT","587"))
    MAIL_USE_TLS=os.environ.get("MAIL_USE_TLS","true").lower() in ["true","on","1"]
    MAIL_USERNAME= os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")
    MAIL_SUBJECT_PREFIX='[VERTICA]'
    MAIL_SENDER="Admin <vertica@example.com>"
    ADMIN = os.environ.get("ADMIN")
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    REMEMBER_COOKIE_DURATION=timedelta(minutes=30)

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" 

class ProductionConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data.sqlite")

config= {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
    }