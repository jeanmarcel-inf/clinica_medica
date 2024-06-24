from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("agendamentos", views.appointments_list, name="appointments"),
    path("perfil", views.profile, name="profile"),
    path('agendar_consulta/<int:medico_id>/', views.make_appointment, name="agendar_consulta"),
]
