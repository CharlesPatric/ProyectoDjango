from django.urls import path
from . import views   #referencia al mismo archivo
from .views import Saludovista,EsparVista # para que funcione la vista clase
urlpatterns = [
    
    path('bienvenido/',views.bienvenido),
    # aca registraremos las urls de otras aplicaciones
    path('ver/<int:numero>/',views.es_par),
    path('sal/<str:nombre>/',Saludovista.as_view() ),# vista basada en clase
    path('par/<int:numero>/',EsparVista.as_view() )# vista basada en clase
]
