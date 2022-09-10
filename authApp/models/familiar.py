from django.db import models
from.usuario import Usuario
from.paciente import Paciente

class Familiar(models.Model):
    id_familiar=models.AutoField(primary_key=True)
    id_paciente=models.ForeignKey(Paciente,related_name='familiar',on_delete=models.CASCADE)
    username=models.ForeignKey(Usuario,related_name='familiar',on_delete=models.CASCADE,unique=True)
    parentesco=models.CharField('Parentesco',max_length=15)
    correo=models.EmailField('Correo',max_length=15)
