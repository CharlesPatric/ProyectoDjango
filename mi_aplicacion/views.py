from django.shortcuts import render
from django.http import HttpResponse   # importando respuestas sin s
from datetime import datetime

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo Cruel!!!!")

def pato(request):
    return HttpResponse("Cuac")
def saludo(request,nombre):
    return HttpResponse(f"hola {nombre}")
#vista que utiliza la plantilla hola.html
def usando_plantillas(request,nombre):
    diccionario = {
    'nombre':nombre,
    'edad': 24,
    'fecha': datetime.now()
        
    }
    return render(request,'mi_aplicacion/hola.html',diccionario)
                #return render( reques donde que )

def usando_otraplanilla(request,datos):
    diccionario={
        'codigo':datos,
        'titulo':'mi nombre es la vida',
    }
    return render(request,'mi_aplicacion/prueba.html',diccionario)

def lista_productos(request):
    productos=[
        {'nombre':'monitor','precio':1250},
        {'nombre':'mouse','precio':120},
        {'nombre':'teclado','precio':200},
    ]
    return render(request,'mi_aplicacion/productos.html',{'productos':productos})

def inicio(request):
    datos_sitio ={
        'Mensaje':'Hola',
        'fecha': datetime.now()
    }
    return render(request,'mi_aplicacion/index.hml',datos_sitio)