from django.shortcuts import render
from django.http import HttpResponse
from django.views import View # importamos para 
# Create your views here.
# vista basada en funciones 
def bienvenido (request):
    return HttpResponse('<h1>Bienvenido a mi otra aplicación</h1>')

def es_par(request,numero):
    # de un número entero ver cual es par o impar
    if numero % 2 ==0:
        return HttpResponse(F"El número {numero} es par ")
    else:
        return HttpResponse(f"El número {numero} es impar")
    
#vista basada en clases
class Saludovista(View):
    def get(self, request,nombre):
        return HttpResponse(f"hola {nombre} saludo desde una clase")
    
class EsparVista(View):
    def get(self, request,numero):
        if numero % 2 ==0:
            return HttpResponse(F"El número {numero} es par ")
        else:
            return HttpResponse(f"El número {numero} es impar")
    