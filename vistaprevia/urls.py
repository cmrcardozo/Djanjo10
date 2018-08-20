from django.conf.urls import url

from vistaprevia import views
from vistaprevia.views import Home, CargarImagen

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^cargar/', CargarImagen.as_view(), name='cargar'),
]
