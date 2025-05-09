from django.db import models

# Create your models here.
class Curso(models.Model): # Uno    
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio =models.DateField()
    
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model): # Muchos
    
    ci = models.CharField(max_length=15,primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True) 
    cursoFk = models.ForeignKey(Curso,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


    
    
   
   