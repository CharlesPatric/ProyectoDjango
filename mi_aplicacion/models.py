from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField(unique=True)
   
   