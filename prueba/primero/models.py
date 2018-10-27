from django.db import models
# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.nombre


SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'No Definido')
)


class Persona(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)	
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to="uploads")
    #nombre = models.CharField(max_length=100)
    #apellido = models.CharField(max_length=100)


class Blog(models.Model):
    titulo = models.CharField("El titulo", max_length=100)
    contenido = models.TextField(blank=True, null=True, default='aqui iba el contenido')

    def comentarios(self):
        return Comentario.objects.filter(blog=self)	

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    contenido = models.CharField(max_length=250)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.contenido
