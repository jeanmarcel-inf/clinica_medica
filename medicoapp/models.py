from django.db import models
from authentication.models import User

class Especialidade(models.Model):
    description = models.CharField(max_length=50, verbose_name="Descrição")

    def __str__(self):
        return self.description

class Medico(User):
    crm = models.CharField(max_length=20, verbose_name="CRM")
    especialidades = models.ManyToManyField(Especialidade, verbose_name="Especialidades")

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return self.get_full_name()

    def get_especialidade(self):
        return self.especialidades.first() if self.especialidades.exists() else None
