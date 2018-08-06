from rest_framework import serializers
from .models import objetivo


class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = objetivo
        fields = '__all__'
