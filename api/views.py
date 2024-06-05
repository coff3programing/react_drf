from rest_framework import viewsets
from .models import LaboratoriosModel, MarcasModel, ActivosModel
from .serializers import LaboratorioSerializer, MarcaSerializer, ActivoSerializer


class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = LaboratoriosModel.objects.all()
    serializer_class = LaboratorioSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = MarcasModel.objects.all()
    serializer_class = MarcaSerializer


class ActivoViewSet(viewsets.ModelViewSet):
    queryset = ActivosModel.objects.all()
    serializer_class = ActivoSerializer
