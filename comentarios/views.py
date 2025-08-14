from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentario
from posts.models import Post
from .forms import ComentarioForm

def agregar_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('detalles_post', post_id=post.id)
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/form_comentario.html', {'form': form, 'post': post})