from rest_framework import serializers
from .models import Datosformulario
from .models import formularios
from .models import objetivos_gestion
from ..responsablesInformacion.serializers import personal_Cargo_UnidadSerializer
from ..responsablesInformacion.serializers import cargoSerializer


class DatosformularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datosformulario
        fields = '__all__'

# class FormularioObjetivosGestionSerializer(serializers.ModelSerializer):
    
#     afiliado = personalSerializer(read_only=True)
#     medico = MedicoSerializer(read_only=True)
#     class Meta:
#         model = OrdenLaboratorio
#         fields = '__all__'

class formulariosRespoCargoSerializer(serializers.ModelSerializer):
    ResponsableInformacion = personal_Cargo_UnidadSerializer(read_only=True)
    cargo=cargoSerializer(read_only=True)
    class Meta:
        model = formularios
        fields = '__all__'

class objetivos_gestion_FormSerializer(serializers.ModelSerializer):
    # Formularios = formulariosRespoCargoSerializer(read_only=True)
    class Meta:
        model = objetivos_gestion
        fields = '__all__'

class formulariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = formularios
        fields = '__all__'

class objetivos_gestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = objetivos_gestion
        fields = '__all__'




