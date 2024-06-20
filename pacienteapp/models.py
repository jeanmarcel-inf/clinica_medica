from django.db import models
from authentication.models import User
from medicoapp.models import Medico 

# Create your models here.

class Paciente(User):
    cellphone_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

class StatusConsulta(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Consulta(models.Model):
    patient = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    description = models.TextField(max_length=200)
    status = models.ForeignKey(StatusConsulta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.medico.first_name + ' consulta: ' + self.patient.first_name
