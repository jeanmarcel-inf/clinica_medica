from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            MinLengthValidator(11),
            RegexValidator(r'^\d{11}$', message='CPF deve conter 11 dígitos.')
        ],
        help_text='Digite seu CPF (somente números).'
    )
    date_of_birth = models.DateField(null=True, blank=True, help_text='Formato: AAAA-MM-DD')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf', 'date_of_birth']

    def __str__(self):
        return self.email