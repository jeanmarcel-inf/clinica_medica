from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from .models import Medico
from pacienteapp.models import Consulta, Paciente, StatusConsulta
from django.db.models import Q

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

        # Calcular total de consultas finalizadas
        status_concluido = StatusConsulta.objects.get(title="Concluído")
        consultas_finalizadas = consultas.filter(status=status_concluido)
        total_consultas_finalizadas = consultas_finalizadas.count()

        return render(request, "medicoapp/pages/dashboard.html", {
            "medico": medico,
            "total_consultas": total_consultas,
            "consultas_hoje": consultas_hoje,
            "today": today,
            "total_pacientes": total_pacientes,  # Passando a contagem total de pacientes para o template
            "total_consultas_finalizadas": total_consultas_finalizadas  # Passando o total de consultas finalizadas para o template
        })
    except Medico.DoesNotExist:
        return HttpResponse("Médico não encontrado.", status=404)
    
def appointments(request):
    user = request.user
    query = request.GET.get('q', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    status_title= request.GET.get('status', '')

    try:
        medico = Medico.objects.get(id=user.id)  # Assuming Medico extends User
        consultas = Consulta.objects.filter(medico=medico)

        # Atualizar status das consultas conforme necessário
        agora = timezone.now()
        status_agendado = StatusConsulta.objects.get(title="Agendado")
        status_concluido = StatusConsulta.objects.get(title="Concluído")
        consultas_finalizadas = consultas.filter(status=status_concluido)
        total_consultas_finalizadas = consultas_finalizadas.count()

        consultas_agendadas = consultas.filter(status=status_agendado, date_time__lt=agora)
        for consulta in consultas_agendadas:
            consulta.status = status_concluido
            consulta.save()

        if query:
            consultas = consultas.filter(Q(patient__first_name__icontains=query) | Q(patient__last_name__icontains=query))
        
        if start_date:
            consultas = consultas.filter(date_time__date__gte=start_date)
        
        if end_date:
            consultas = consultas.filter(date_time__date__lte=end_date)
        
        if status_title:
            consultas = consultas.filter(status__title=status_title)

        total_consultas = consultas.count()
        
        # Calculating total unique patients
        total_pacientes = consultas.values('patient').distinct().count()
        
        # Get all statuses for the filter dropdown
        status_list = StatusConsulta.objects.all()

        return render(request, "medicoapp/pages/appointments.html", {
            "medico": medico,
            "consultas": consultas,
            "total_consultas": total_consultas,
            "total_pacientes": total_pacientes,
            "query": query,
            "start_date": start_date,
            "end_date": end_date,
            "status": status_title,
            "status_list": status_list,
            "total_consultas_finalizadas": total_consultas_finalizadas
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
