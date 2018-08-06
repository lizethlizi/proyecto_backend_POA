from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

from .models import personal
from .serializers import personalSerializer
from .models import cargo
from .serializers import cargoSerializer

class ListaPersonal(APIView):
    def get(self, request,format=None):
        Personal = personal.objects.all()
        data = personalSerializer(Personal, many=True).data
        return Response(data)

class ListaCargos(APIView):
    def get(self, request,format=None):
        Cargos = cargo.objects.all()
        data = cargoSerializer(Cargos, many=True).data
        return Response(data)