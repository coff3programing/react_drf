from rest_framework import serializers
from .models import LaboratoriosModel, MarcasModel, ActivosModel


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoriosModel
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcasModel
        fields = '__all__'


class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivosModel
        fields = '__all__'

