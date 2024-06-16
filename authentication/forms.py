from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use o seu modelo de usuário personalizado
        fields = ('email', 'cpf', 'date_of_birth')  # Inclua o campo CPF aqui
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].required = True  # Se você quiser que o CPF seja obrigatório


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User  # Use o seu modelo de usuário personalizado
        fields = ('email', 'cpf', 'date_of_birth')  # Inclua o campo CPF aqui