from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Paciente, Consulta
from medicoapp.models import Medico
from .forms import ConsultaCreateForm 

# Create your views here.


def index(request):
    return render(request, "pacienteapp/pages/index.html")


def home(request):
    return render(request, "pacienteapp/pages/home.html")


def appointments_list(request):
    medicos = Medico.objects.all()
    form = ConsultaCreateForm()
    return render(request, "pacienteapp/pages/appointments.html", {"medicos": medicos, "form": form })
    # modal_items = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00' ]
    # form = ConsultaCreateForm()

def make_appointment(request, medico_id):
    medico = Medico.objects.get(pk=medico_id)
    if request.method == 'POST':
        form = ConsultaCreateForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            patient = Paciente.objects.get(cpf=request.user.cpf)
            consulta.patient = patient
            consulta.medico = medico
            consulta.status_id = 1
            consulta.date_time = form.cleaned_data['date_time']
            consulta.save()
    else:
        form = ConsultaCreateForm(initial={'medico': medico_id})
    return redirect('/paciente/agendamentos')

def profile(request):
    patient = Paciente.objects.get(pk=request.user.id)
    consultas = Consulta.objects.filter(patient = patient)
    return render(request, "pacienteapp/pages/profile.html", {'consultas': consultas, 'patient': patient})
