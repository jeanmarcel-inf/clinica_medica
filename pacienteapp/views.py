from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "pacienteapp/pages/index.html")


def home(request):
    return render(request, "pacienteapp/pages/home.html")


def appointments(request):
    return render(request, "pacienteapp/pages/appointments.html")


def profile(request):
    return render(request, "pacienteapp/pages/profile.html")
