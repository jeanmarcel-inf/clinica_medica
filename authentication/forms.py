from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Email',
        'id': 'login-email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Password',
        'id': 'login-password'
    }))

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Email',
        'id': 'login-email'
    }))