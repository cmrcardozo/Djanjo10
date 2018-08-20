from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from vistaprevia.models import Producto
from django.shortcuts import redirect
from vistaprevia.forms import CargarForm
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.generic import View


class Home(View):

    template = 'vistaprevia/index.html'

    def get(self, request, *args, **kwargs):

        params = {}
        params ['para_minorista'] = { 'tipo_usuario' : 'minorista' , 'incremento' : '25'}
        params['para_mayorista'] = { 'tipo_usuario' : 'mayorista' , 'incremento' : '10'}
        return render(request, self.template, params)


class CargarImagen(View):

    template = 'vistaprevia/formulario.html'

    def get(self, request, *args, **kwargs):
        form = CargarForm()
        params = {}
        params ['form'] = form
        return render(request, self.template, params)


    def post(self, request, *args, **kwargs):
        form = CargarForm(request.POST, request.FILES)
        params = {}
        params ['form'] = form
        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            ruta_imagen = form.cleaned_data['ruta_imagen']

            newdoc = Producto(producto = producto, fecha_publicacion = fecha_publicacion, ruta_imagen = ruta_imagen)
            newdoc.save()
            return redirect("index")
        else:
            return render(request, 'vistaprevia/formulario.html', {'form': form})