from flask import Flask
from config import config
from flask_celery import Celery

celery = Celery()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    celery.init_app(app)

    from .views import view as view_blueprint
    app.register_blueprint(view_blueprint)

    return app
