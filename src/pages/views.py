import os

from django import get_version
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django_redis import get_redis_connection
from django.db import connection


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"]
    }

    return render(request, "pages/home.html", context)


def up(request):
    get_redis_connection().ping()
    connection.ensure_connection()

    return HttpResponse("")
