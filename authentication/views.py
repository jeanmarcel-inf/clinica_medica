from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login")
    else:
        form = CustomUserCreationForm()
    return render(request, "authentication/pages/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/auth/success")
    else:
        form = CustomAuthenticationForm()
    return render(request, "authentication/pages/login.html", {"form": form})


def password_reset(request):
    return render(request, "authentication/pages/password-reset.html")
