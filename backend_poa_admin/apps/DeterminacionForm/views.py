from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Datosformulario
from .serializers import DatosformularioSerializer
from .models import formularios
from .serializers import formulariosSerializer
from .models import objetivos_gestion
from .serializers import objetivos_gestionSerializer
from .serializers import objetivos_gestion_FormSerializer
from .serializers import formulariosRespoCargoSerializer

class DatosFormularios(APIView):
    def get(self, request):
        datos = Datosformulario.objects.all()[:20]
        #medico=Medico.objects.all()[:20]
        data = DatosformularioSerializer(datos, many=True).data
        return Response(data)

class ListaFormularios(APIView):
    def get(self, request,format=None):
        Formulario = formularios.objects.all()
        #medico=Medico.objects.all()[:20]
        serializer = formulariosRespoCargoSerializer(Formulario, many=True)
        return Response(serializer.data)

class ListaObjetivosGestion(APIView):
    def get(self, request):
        Objetivo = objetivos_gestion.objects.all()
        #medico=Medico.objects.all()[:20]
        data = objetivos_gestion_FormSerializer(Objetivo, many=True).data
        return Response(data)

class GuardarFormulario(APIView):
     def post(self, request):
            
            Gestion = request.data.get("Gestion")
            Fecha=request.data.get("Fecha")
            ResponsableInformacion=request.data.get("ResponsableInformacion")
            Cargo=request.data.get("Cargo")

            data = {'Gestion': Gestion,'Fecha':Fecha,'ResponsableInformacion':ResponsableInformacion,'Cargo':Cargo}  #medico como ide tiene q ir el mismo q con el que pusimos en el modelo
            serializer = formulariosSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuardarObjetivosGestion(APIView):
     def post(self, request):
            Descripcion = request.data.get("Descripcion")
            Resultados=request.data.get("Resultados")
            Beneficiarios=request.data.get("Beneficiarios")
            Formularios=request.data.get("Formularios")
            data = {'Descripcion': Descripcion,'Resultados':Resultados,'Beneficiarios':Beneficiarios,'Formularios':Formularios}  #medico como ide tiene q ir el mismo q con el que pusimos en el modelo
            serializer = objetivos_gestionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

