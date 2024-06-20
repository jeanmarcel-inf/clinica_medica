from django.db import models
from authentication.models import User

# Create your models here.

class Especialidade(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Medico(User):
    crm = models.CharField(max_length=20)
    especialidades = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.get_full_name()
    
    def get_especialidade(self):
        return self.especialidades.first()
    