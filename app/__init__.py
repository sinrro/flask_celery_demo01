import time

from flask import Flask
from config import config, celery_config
from celery import Celery

celery = Celery(__name__, backend=celery_config['CELERY_RESULT_BACKEND'], broker=celery_config['CELERY_BROKER_URL'])


def register_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask


@celery.task()
def add_together(a, b):
    time.sleep(10)
    return a + b


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    register_celery(app)

    from .views import view as view_blueprint
    app.register_blueprint(view_blueprint)

    return app
