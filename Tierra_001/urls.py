from django.urls import path
from . import views

urlpatterns = [
    path('', views.archivo, name='archivo'),
    path('about', views.selfo, name='selfo'),
    path('trabajos', views.trabajos, name='trabajos'),
    path('escrit', views.escrit, name='escrit'),
    path('trabajos1', views.trabajos1, name='trabajos1'),
    path('trabajos2', views.trabajos2, name='trabajos2'),


]