from django.urls import path
from .views import ListaObjetivos,GuardarObjetivoGestion

urlpatterns = [
    path('objetivos/', ListaObjetivos.as_view(),name="ListaObjetivos"),
    #path('<int:pk>/', views.DetailTodo.as_view()),
    path('guardar/', GuardarObjetivoGestion.as_view(),name="GuardarObjetivoGestion")
    
]