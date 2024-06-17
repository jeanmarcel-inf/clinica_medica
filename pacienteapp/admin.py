from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Paciente, Consulta, StatusConsulta

# Register your models here.

class PacienteAdmin(UserAdmin):
    model = Paciente
    list_display = ['email', 'first_name', 'last_name', 'gender', 'cpf', 'date_of_birth',  'is_active']
    list_filter = [ 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cpf', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'cpf', 'date_of_birth', 'gender'),
        }),
    )
    search_fields = ('email', 'cpf')
    ordering = ('email',)

admin.site.register(Paciente, PacienteAdmin)

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "medico", "date_time", "description", "status")
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(StatusConsulta)