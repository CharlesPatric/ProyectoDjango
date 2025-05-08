#from django.contrib import admin
from django.urls import path
from . import views   #referencia al mismo archivo

urlpatterns = [
    path('hola/',views.hola_mundo),#registradon la vista para holamundo
    path('patin/',views.pato),
    path('s/<str:nombre>/',views.saludo),
    path('plantilla/<str:nombre>',views.usando_plantillas),
    path('plani/<int:datos>',views.usando_otraplanilla),
    path('produ/',views.lista_productos),
    path('',views.inicio),
]
