from django.urls import path
from .views import ListaPersonal,ListaCargos

urlpatterns = [
    path('ListaPersonal/', ListaPersonal.as_view(),name="ListaPersonal"),
    path('ListaCargos/', ListaCargos.as_view(),name="ListaCargos"),
]