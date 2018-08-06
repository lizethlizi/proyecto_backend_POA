from django.urls import path
from .views import DatosFormularios,ListaFormularios,ListaObjetivosGestion,GuardarObjetivosGestion,GuardarFormulario

urlpatterns = [
    path('DatosFormulario/', DatosFormularios.as_view(),name="DatosFormularios"),
    path('ListaFormularios/', ListaFormularios.as_view(),name="ListaFormularios"),
    path('ListaObjetivosGestion/', ListaObjetivosGestion.as_view(),name="ListaObjetivosGestion"),
    #path('<int:pk>/', views.DetailTodo.as_view()),
    path('Registrar/', GuardarObjetivosGestion.as_view(),name="GuardarObjetivosGestion"),
    path('RegistrarForm/', GuardarFormulario.as_view(),name="GuardarFormulario")
]