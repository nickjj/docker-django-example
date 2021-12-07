import os

from django import get_version
from django.conf import settings
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from redis import Redis


redis = Redis.from_url(settings.REDIS_URL)


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)


def up(request):
    redis.ping()
    connection.ensure_connection()

    return HttpResponse("")
