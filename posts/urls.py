from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_post, name='nuevo_post'),
    path('post/<int:post_id>/', views.detalles_post, name='detalles_post'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),   
]