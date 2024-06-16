from django.contrib import admin
from .models import Paciente, Consulta, StatusConsulta

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "cpf", "email", "gender", "address" )

admin.site.register(Paciente, PacienteAdmin)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "medico", "date_time", "description", "status")
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(StatusConsulta)