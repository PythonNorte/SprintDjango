from django.db import models

# Create your models here.


class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()

class Comentario(models.Model):
    contenido = models.CharField(max_length=250)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
