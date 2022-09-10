from django.db import models
from.usuario import Usuario

class Personal_salud(models.Model):
    id_pSalud=models.AutoField(primary_key=True)
    username=models.ForeignKey(Usuario,related_name='pSalud',on_delete=models.CASCADE,unique=True)
    rol=models.CharField('Rol',max_length=15)
    especialidad=models.CharField('Especialidad',max_length=20)
    
