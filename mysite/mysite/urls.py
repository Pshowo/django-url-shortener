
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', include('website.urls')),
    path("", include('api.urls')),
]
