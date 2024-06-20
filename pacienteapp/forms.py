from django import forms
from .models import Paciente, Consulta
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PacienteCreationForm(UserCreationForm):

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
        model = Paciente
        fields = ('first_name', 'last_name', 'email', 'cpf', 'date_of_birth', 'cellphone_number', 'gender')
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
            }, choices=[('', 'Selecione o gênero')] + Paciente.GENDER_CHOICES),
            'cellphone_number': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Número de Celular',
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].required = True 

class PacienteChangeForm(UserChangeForm):    
    class Meta:
        model = Paciente  
        fields = ('email', 'cpf', 'date_of_birth', 'gender', 'cellphone_number')  


class ConsultaCreateForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ("date_time", "description")
        labels = {
            'date_time': 'Nome do Item',
        }
        widgets = {
            'date_time': forms.RadioSelect(attrs={
                'class': 'btn-check',
                'checked': True
            }),
        }
