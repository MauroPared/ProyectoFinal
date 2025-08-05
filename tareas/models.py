from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=100)
    
    
class Post:
    Titulo = models.CharField(max_length= 200)

    
    