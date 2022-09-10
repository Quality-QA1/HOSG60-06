from django.db import models
from.paciente import Paciente

class Hclinica(models.Model):
    id_historiaclinica=models.AutoField(primary_key=True)
    id_paciente=models.ForeignKey(Paciente,related_name='historiaclinica',on_delete=models.CASCADE)
    sugerenciacuidado=models.CharField('Sugerenciacuidado',max_length=200)
    diagnostico=models.CharField('Diagnostico',max_length=200)
    entorno=models.CharField('Entorno',max_length=100)
    fechasugerencia=models.DateField()
    descripcion=models.CharField('Descripcion',max_length=300)
    
