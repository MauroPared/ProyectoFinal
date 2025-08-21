from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='categorias_lista'),
    path('<int:categoria_id>/', views.posts_por_categoria, name='posts_por_categoria'),
]

