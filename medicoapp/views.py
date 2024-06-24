from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Medico
from django.http import HttpResponse

# Create your views here.


def home(request):
    user = request.user
    try:
        medico = Medico.objects.get(id=user.id)  # Assuming Medico extends User
        return render(request, "medicoapp/pages/dashboard.html", {"user": user, "medico": medico})
    except Medico.DoesNotExist:
        return HttpResponse("Médico não encontrado.", status=404)

def appointments(request):
    return render(request, "medicoapp/pages/appointments.html")

def patients(request):
    return render(request, "medicoapp/pages/patients.html")
