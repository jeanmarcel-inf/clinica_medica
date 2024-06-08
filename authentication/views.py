from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "authentication/pages/login.html")


def register(request):
    return render(request, "authentication/pages/register.html")


def password_reset(request):
    return render(request, "authentication/pages/password-reset.html")
