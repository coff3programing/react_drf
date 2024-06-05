from django.contrib import admin
from .models import LaboratoriosModel, MarcasModel, ActivosModel

# Register your models here.
admin.site.register(LaboratoriosModel)
admin.site.register(MarcasModel)
admin.site.register(ActivosModel)