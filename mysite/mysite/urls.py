
from django.contrib import admin
from django.urls import path, include
from api import views 
app_name = "main"
urlpatterns = [
    path('statistics/', include('website.urls')),
    path("v1/api/", include('api.urls')),
    path('<str:short_url>/', views.redirect_url, name="url-redirect"),
]
