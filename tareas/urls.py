from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Inicio,name='Blog-Inicio'),
    path('Acerca/', views.Acerca_De, name='Acerca'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('Registrarse', views.Registrarse, name='Registrarse'),
    path('post/<int:post_id>/', views.detalles_post, name='detalles_post'),
    path('nuevo/', views.nuevo_post, name='nuevo_post'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='tareas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('registro/', views.Registrarse, name='registro'),
]
