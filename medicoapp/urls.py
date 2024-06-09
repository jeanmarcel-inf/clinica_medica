from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home),
    path("consultas", views.appointments),
    path("pacientes", views.patients),
]
