from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Especialidade)

class MedicoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "cpf", "crm", "get_especialidades" )

    # --- INFO: Método get para campo especialidades dentro de Medico, busca por toda instancia de Especialidade associada com o id do Medico.
    def get_especialidades(self, obj):
        return [especialidade.description for especialidade in obj.especialidades.all()]
    
    # Renomear a coluna get_especialidades
    get_especialidades.short_description = "especialidades"
    
admin.site.register(Medico, MedicoAdmin)