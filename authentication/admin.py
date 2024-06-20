from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'first_name', 'last_name', 'gender', 'cpf', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cpf', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'cpf', 'date_of_birth', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'cpf')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)