from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from primero.models import Blog, Comentario


# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    publicaciones = Blog.objects.all()
    data = {
	"titulo": "DJango",
	"publicaciones": publicaciones,	
	"comentario": Comentario.objects.all()[0],
    }
    return HttpResponse(template.render(data))



