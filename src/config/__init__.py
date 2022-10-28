# This will make sure the app is always imported when Django starts so that
# shared_task will use this app. This is taken from Celery's docs at:
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
from config.celery import app as celery_app

__all__ = ("celery_app",)
