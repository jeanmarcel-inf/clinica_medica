from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "pages/index.html")


def home(request):
    return render(request, "pages/home.html")


def agenda_consultas(request):
    return render(request, "pages/agendamentos.html")
