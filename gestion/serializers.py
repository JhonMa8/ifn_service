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

from rest_framework import serializers
from .models import RegistroCampo

class RegistroCampoSerializer(serializers.ModelSerializer):
    creado_por = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = RegistroCampo
        fields = '__all__'
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion', 'creado_por')        
