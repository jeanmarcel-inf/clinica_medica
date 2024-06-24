from django.urls import path
from . import views

app_name = 'medico'

urlpatterns = [
    path("home", views.home, name='home'),
    path("consultas", views.appointments, name='appointments' ),
    path("pacientes", views.patients, name='patients'),
]
