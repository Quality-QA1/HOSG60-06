from django.contrib import admin
from .models.familiar import Familiar
from .models.hclinica import Hclinica
from .models.paciente import Paciente
from .models.pSalud import Personal_salud
from .models.sigvitales import Sigvitales
from .models.usuario import Usuario




# Register your models here.


admin.site.register(Familiar)
admin.site.register(Hclinica)
admin.site.register(Paciente)
admin.site.register(Personal_salud)
admin.site.register(Sigvitales)
admin.site.register(Usuario)
