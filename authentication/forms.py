from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Senha',
        })
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmar Senha',
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'cpf', 'date_of_birth', 'gender')
        labels = {
            'gender': 'Sexo'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Nome',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Sobrenome',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Email',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'CPF',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Data de Nascimento',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Sexo',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].required = True  # Se você quiser que o CPF seja obrigatório

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User  # Use o seu modelo de usuário personalizado
        fields = ('email', 'cpf', 'date_of_birth', 'gender')  # Inclua o campo CPF aqui


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