from django.urls import path
from . import views

urlpatterns = [
    path('eliminar/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),
    path('editar/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),        
    ]