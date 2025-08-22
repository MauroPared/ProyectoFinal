from django.shortcuts import render, get_object_or_404
from .models import Categoria
from posts.models import Post

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista_categorias.html', {'categorias': categorias})

def posts_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    posts = categoria.posts.all()
    return render(request, 'categorias/posts_por_categoria.html', {
        'categoria': categoria,
        'posts': posts
    })