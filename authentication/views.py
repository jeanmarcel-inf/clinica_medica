from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from pacienteapp.forms import PacienteCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = PacienteCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/paciente/home")
    else:
        form = PacienteCreationForm()
    return render(request, "authentication/pages/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Adicionar rota dinâmica para direcionar usuarios especificos para cada aplicação (Paciente - /paciente, Medico - /medico)
            return redirect("/paciente/home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "authentication/pages/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/paciente/")

def password_reset(request):
    return render(request, "authentication/pages/password-reset.html")
