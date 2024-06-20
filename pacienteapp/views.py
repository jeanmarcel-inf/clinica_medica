from django.shortcuts import render
from django.utils import timezone
from .models import Paciente, Consulta
from .forms import ConsultaCreateForm 

# Create your views here.


def index(request):
    return render(request, "pacienteapp/pages/index.html")


def home(request):
    return render(request, "pacienteapp/pages/home.html")


def appointments(request):
    consultas = Consulta.objects.all()
    modal_items = ['8:00', '10:00', '12:00', '14:00', '15:00', '17:00', '19:00', ]
    form = ConsultaCreateForm()

    return render(request, "pacienteapp/pages/appointments.html", {"consultas": consultas, "modal_items": modal_items, "form": form})


def profile(request):
    user = request.user
    print(user)
    consultas = Consulta.objects.filter(patient = request.user)
    print(consultas)
    return render(request, "pacienteapp/pages/profile.html", {'consultas': consultas})
