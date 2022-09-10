from authApp.models.sigvitales import Sigvitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sigvitales
        fields=('id_paciente','oximetria','frecuenciarespiratoria','frecuenciacardiaca','temperatura','glicemias','presionarterial','fechayhora')
        