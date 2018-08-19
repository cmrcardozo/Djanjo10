#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import RequestContext, loader

# Create your views here.
#def index(request):
#	contenido = { 'nombre_sitio': 'Mis Libros Online' }
#	para_minorista = { 'tipo_usuario' : 'minorista', 'incremento' : '25'}
#	para_mayorista = { 'tipo_usuario' : 'mayorista', 'incremento' : '10'}
#	return render(request, 'vistaprevia/index.html', {'contenido':contenido, 'para_minorista':para_minorista, 'para_mayorista':para_mayorista})
#	#return render(request, 'vistaprevia/index.html', contenido)
from vistaprevia.models import Producto
from django.shortcuts import redirect
from vistaprevia.forms import CargarForm

def cargar_imagen(request):
	if request.method == 'POST':
		form = CargarForm(request.POST, request.FILES)
	if form.is_valid():
		producto = form.cleaned_data['producto']
		fecha_publicacion = form.cleaned_data['fecha_publicacion']
		ruta_imagen = form.cleaned_data['ruta_imagen']
		newdoc = Producto(producto = producto, fecha_publicacion = fecha_publicacion, ruta_imagen = ruta_imagen)
		newdoc.save()
		return redirect("index")
	else:
		form = CargarForm()
	return render(request, 'vistaprevia/formulario.html', {'form': form})