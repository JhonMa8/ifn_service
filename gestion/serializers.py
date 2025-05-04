from rest_framework import serializers
from .models import Departamento, Municipio, Coordenada, Brigada, Parcela, ConteoArbol

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class CoordenadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenada
        fields = '__all__'

class BrigadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brigada
        fields = '__all__'

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = '__all__'

class ConteoArbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteoArbol
        fields = '__all__'
