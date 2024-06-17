from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class MedicoAdmin(UserAdmin):
    def get_especialidades(self, obj):
        return [especialidade.description for especialidade in obj.especialidades.all()]
    
    get_especialidades.short_description = "especialidades"
    
    model = Medico
    list_display = ['email', 'first_name', 'last_name', 'gender', 'crm', 'get_especialidades',  'is_active']
    list_filter = [ 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cpf', 'crm', 'date_of_birth', 'gender', 'especialidades')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'crm', 'cpf', 'date_of_birth', 'gender', 'especialidades'),
        }),
    )
    search_fields = ('email', 'cpf')
    ordering = ('email',)
    
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade)