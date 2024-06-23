from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomAuthenticationForm
from pacienteapp.forms import PacienteCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
from django.contrib.auth.models import Group


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
            user = form.get_user()
            login(request, user)
            
            if Group.objects.filter(name='Médicos', user=user).exists():
                return redirect(reverse('medico:home'))
            elif Group.objects.filter(name='Pacientes', user=user).exists():
                return redirect(reverse('paciente:home'))
            else:
                # Handle users not in any specific group
                return redirect(reverse('authentication:login'))
    else:
        form = CustomAuthenticationForm()
    return render(request, "authentication/pages/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/paciente/")

def password_reset(request):
    return render(request, "authentication/pages/password-reset.html")

class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = CustomPasswordResetForm