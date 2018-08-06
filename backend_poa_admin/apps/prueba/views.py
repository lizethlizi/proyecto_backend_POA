from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import objetivo
from .serializers import ObjetivoSerializer

class ListaObjetivos(APIView):
    def get(self, request):
        Objetivo = objetivo.objects.all()[:20]
        #medico=Medico.objects.all()[:20]
        data = ObjetivoSerializer(Objetivo, many=True).data
        return Response(data)

class GuardarObjetivoGestion(APIView):
    # def post(self, request, id_medico):
     def post(self, request):
            # Gestion=request.data.get("Gestion")
            # fecha = request.data.get("fecha")
            Descripcion = request.data.get("Descripcion")
            Resultados=request.data.get("Resultados")
            Beneficiarios=request.data.get("Beneficiarios")
            data = {'Descripcion': Descripcion,'Resultados':Resultados,'Beneficiarios':Beneficiarios}  #medico como ide tiene q ir el mismo q con el que pusimos en el modelo
            serializer = ObjetivoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ListaObjetivos(APIView):
   
#     """LISTA TODOS LOS REGISTROS"""
#     def get(self, request, format=None):
#         snippets = ExamenGeneralOrina.objects.all()
#         serializer = ExamenGeneralOrinaSerializer(snippets, many=True)
#         return Response(serializer.data)