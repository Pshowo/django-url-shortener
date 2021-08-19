from django.shortcuts import render
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

# appname = "shortener"
router = routers.DefaultRouter()
router.register(r'urls', views.UrlsViewSet,basename='MyModel')
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
]