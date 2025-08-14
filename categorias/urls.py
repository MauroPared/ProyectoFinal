from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('<int:categoria_id>/', views.posts_por_categoria, name='posts_por_categoria'),
]

