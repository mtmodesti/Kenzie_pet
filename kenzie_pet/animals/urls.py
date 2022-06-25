from django.urls import path
from . import views
from rest_framework.views import APIView, Response


urlpatterns = [
    path("", views.HomeView.as_view()),
    path("animals/", views.AnimalView.as_view()),
    path("animals/<int:animal_id>/", views.AnimalIdView.as_view()),
]