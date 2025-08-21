from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Acerca/', views.Acerca_De, name='Acerca'),
    path('Contacto/', views.Contacto, name='Contacto'),
]