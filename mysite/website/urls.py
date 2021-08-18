from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path("", views.Urls.as_view(), name="url_list"),
]