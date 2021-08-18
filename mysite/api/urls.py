from django.shortcuts import render
from django.urls import path
from . import views

appname = "shortener"

urlpatterns = [
    # Home view
    path("", views.index, name="home"),
    path('<str:short_url>', views.redirect_url, name="redirect")
]