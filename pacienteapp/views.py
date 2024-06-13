from django.shortcuts import render
from medicoapp.models import Medico
from .models import Paciente

# Create your views here.


def index(request):
    return render(request, "pacienteapp/pages/index.html")


def home(request):
    return render(request, "pacienteapp/pages/home.html")


def appointments(request):
    medicos = Medico.objects.all()
    return render(request, "pacienteapp/pages/appointments.html", {"medics": medicos})


def profile(request):
    patients = Paciente.objects.all()
    return render(request, "pacienteapp/pages/profile.html", {"patients": patients})
