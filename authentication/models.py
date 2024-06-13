from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    last_login = None
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=70)
    date_of_birth  = models.DateField(auto_now=False, auto_now_add=False)

    USERNAME_FIELD="name"