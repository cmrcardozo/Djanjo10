from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	contenido = { 'nombre_sitio': 'Mis Libros Online' }
	return render(request, 'vistaprevia/index.html', contenido)