from django.urls import path

from up import views

urlpatterns = [
    path("", views.index, name="index"),
    path("databases", views.databases, name="databases"),
]
