from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apps.config.config import Config

app = Flask(__name__)
db = SQLAlchemy(app)


def create_app(object):
    app.config.from_object(Config)
    return app
