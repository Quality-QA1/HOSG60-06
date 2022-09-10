from authApp.models.hclinica import Hclinica
from rest_framework import serializers

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hclinica
        fields=('id_paciente','sugerenciacuidado','diagnostico','entorno','fechasugerencia','descripcion')