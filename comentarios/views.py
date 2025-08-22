from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm
from .models import Comentario
from posts.models import Post


@login_required
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
    return render(request, 'comentarios/agregar_comentario.html', {'form': form, 'post': post})

@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    # solo el autor o el moderador pueden eliminarlo
    if request.user != comentario.autor and not request.user.is_staff:
        return redirect('detalles_post', post_id=comentario.post.id)
    
    if request.method == 'POST':
        comentario.delete()
        return redirect('detalles_post', post_id=comentario.post.id)
    
    return render(request, 'comentarios/eliminar_comentario.html', {
        'comentario': comentario
    })

    
@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    #solo el autor puede editar
    if request.user != comentario.autor and not request.user.is_staff:
        return redirect('detalles_post', post_id=comentario.post.id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('detalles_post', post_id=comentario.post.id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'comentarios/editar_comentario.html', {
        'form': form,
        'comentario': comentario
    })