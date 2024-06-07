from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("agendamentos", views.appointments, name="appointments"),
    path("perfil", views.profile, name="profile"),
]
