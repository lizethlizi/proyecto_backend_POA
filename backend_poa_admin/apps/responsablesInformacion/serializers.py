from rest_framework import serializers
from .models import personal
from .models import cargo
from .models import unidad

class cargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cargo
        fields = '__all__'

class unidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = unidad
        fields = '__all__'

class personalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = personal
        fields = '__all__'

class personal_Cargo_UnidadSerializer(serializers.ModelSerializer):
    Cargo = cargoSerializer(read_only=True)
    Unidad = unidadSerializer(read_only=True)
    class Meta:
        model = personal
        fields = '__all__'
        