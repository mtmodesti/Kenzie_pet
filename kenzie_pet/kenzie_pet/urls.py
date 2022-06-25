
from django.contrib import admin
from django.urls import path, include
from animals import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("animals.urls")), 
]
