import os


class Config:
    SECRET_KEY = 'hard to guess string'
    SSL_DISABLE = False

    # 子类实现该方法
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}

celery_config = {
    'CELERY_BROKER_URL': 'redis://127.0.0.1:6379/0',
    'CELERY_RESULT_BACKEND': 'redis://127.0.0.1:6379/0'

}
