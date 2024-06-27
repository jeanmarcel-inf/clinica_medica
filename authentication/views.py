from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomAuthenticationForm
from pacienteapp.forms import PacienteCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
from django.contrib.auth.models import Group
from medicoapp.models import Medico
from pacienteapp.models import Paciente

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = PacienteCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("paciente:home")
    else:
        form = PacienteCreationForm()
    return render(request, "authentication/pages/register.html", {"form": form})



def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if user.is_superuser:
                return redirect('/admin/')
            elif Medico.objects.filter(pk=user.id).exists():
                return redirect(reverse('medico:home'))
            elif Paciente.objects.filter(pk=user.id).exists():
                return redirect(reverse('paciente:home'))
    else:
        form = CustomAuthenticationForm()
    return render(request, "authentication/pages/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("paciente:index")

def password_reset(request):
    return render(request, "authentication/pages/password-reset.html")

class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = CustomPasswordResetForm