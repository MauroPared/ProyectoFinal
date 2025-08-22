from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='categorias_lista'),
    path("<slug:slug>/", views.posts_por_categoria, name='posts_por_categoria'),
]

