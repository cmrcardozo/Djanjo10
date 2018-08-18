from django.conf.urls import include,url
from vistaprevia import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
