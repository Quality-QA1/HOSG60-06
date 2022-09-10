from django.db import models
from.paciente import Paciente

class Sigvitales(models.Model):
    id_signosvitales=models.AutoField(primary_key=True)
    id_paciente=models.ForeignKey(Paciente,related_name='signosvitales',on_delete=models.CASCADE)
    oximetria=models.IntegerField(default=0)
    frecuenciarespiratoria=models.IntegerField(default=0)
    frecuenciacardiaca=models.IntegerField(default=0)
    temperatura=models.IntegerField(default=0)
    glicemias=models.IntegerField(default=0)
    presionarterial=models.IntegerField(default=0)
    fechayhora=models.DateTimeField()
    


    
