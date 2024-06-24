from django import forms
from .models import Paciente, Consulta
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import DateInput, RadioSelect
from datetime import datetime

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
    data = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    hora = forms.ChoiceField(widget=RadioSelect)

    class Meta:
        model = Consulta
        fields = ['data', 'hora', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'descriptionArea'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hora'].choices = self.get_time_choices()

    def get_time_choices(self):
        times = []
        for hour in range(8, 17):
            for minute in (0, 30):
                time = f"{hour:02d}:{minute:02d}"
                times.append((time, time))
        return times
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        hora = cleaned_data.get('hora')
        if data and hora:
            date_time = datetime.combine(data, datetime.strptime(hora, "%H:%M").time())
            cleaned_data['date_time'] = date_time
        return cleaned_data
