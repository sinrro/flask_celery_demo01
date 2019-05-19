import time

from app import celery


@celery.task()
def add_together(a, b):
    time.sleep(5)
    return a + b


@celery.task()
def add_together1(a, b):
    time.sleep(15)
    return a + b
