from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from .models import Medico
from pacienteapp.models import Consulta, Paciente
from django.db.models import Q

# Create your views here.

def home(request):
    user = request.user
    try:
        medico = Medico.objects.get(id=user.id)  # Assuming Medico extends User
        today = datetime.now().date()
        consultas_hoje = Consulta.objects.filter(medico=medico, date_time__date=today)
        total_consultas = consultas_hoje.count()

        # Filtrando todas as consultas do médico
        consultas = Consulta.objects.filter(medico=medico)
        total_pacientes = Paciente.objects.filter(consulta__in=consultas).distinct().count()

        return render(request, "medicoapp/pages/dashboard.html", {
            "medico": medico,
            "total_consultas": total_consultas,
            "consultas_hoje": consultas_hoje,
            "today": today,
            "total_pacientes": total_pacientes  # Passando a contagem total de pacientes para o template
        })
    except Medico.DoesNotExist:
        return HttpResponse("Médico não encontrado.", status=404)
    

def appointments(request):
    user = request.user
    query = request.GET.get('q', '')
    try:
        medico = Medico.objects.get(id=user.id)  # Assuming Medico extends User
        consultas = Consulta.objects.filter(medico=medico)
        
        if query:
            consultas = consultas.filter(Q(patient__first_name__icontains=query) | Q(patient__last_name__icontains=query))

        total_consultas = consultas.count()
        
        # Calculating total unique patients
        total_pacientes = consultas.values('patient').distinct().count()
        
        return render(request, "medicoapp/pages/appointments.html", {
            "medico": medico,
            "consultas": consultas,
            "total_consultas": total_consultas,
            "total_pacientes": total_pacientes,
            "query": query,
        })
    except Medico.DoesNotExist:
        return HttpResponse("Médico não encontrado.", status=404)

    
def patients(request):
    user = request.user
    try:
        medico = Medico.objects.get(id=user.id)  # Assuming Medico extends User
        pacientes = Paciente.objects.filter(consulta__medico=medico).distinct()
        return render(request, "medicoapp/pages/patients.html", {"medico": medico, "pacientes": pacientes})
    except Medico.DoesNotExist:
        return HttpResponse("Médico não encontrado.", status=404)
