from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "medicoapp/pages/dashboard.html")

def appointments(request):
    return render(request, "medicoapp/pages/appointments.html")

def patients(request):
    return render(request, "medicoapp/pages/patients.html")
