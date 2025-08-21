from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from comentarios.models import Comentario
from comentarios.forms import ComentarioForm
from django.db.models import Count 


def detalles_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # Obtener todos los comentarios relacionados con este post
    comentarios = post.comentarios.all().order_by('-fecha')
    form_comentario = None # Inicializamos el formulario de comentar    
    if request.method == 'POST':
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            if request.user.is_authenticated:
                nuevo_comentario = form_comentario.save(commit=False)
                nuevo_comentario.post = post
                nuevo_comentario.autor = request.user
                nuevo_comentario.save()
               
                return redirect('detalles_post', post_id=post.id)
    else:
        form_comentario = ComentarioForm()    
    return render(request, 'posts/detalles_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    })


@login_required
def nuevo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.autor = request.user
            nuevo_post.save()
        return redirect('Inicio')
    else:
        form = PostForm()
    return render(request, 'posts/nuevo_post.html', {'form': form})



def lista_posts(request):
    posts = Post.objects.all() # Obtiene todos los posts de la base de datos
    return render(request, 'posts/lista_posts.html', {'posts': posts})

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Verificación de seguridad: solo el autor puede editar el post
    if request.user != post.autor:
       return redirect('detalles_post', post_id=post.id) # Redirige al post si no es el autor
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalles_post', post_id=post.id)              
        else:
            form = PostForm(instance=post)
    return render(request, 'posts/editar_post.html', {'form': form})

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Verificación de seguridad: solo el autor puede eliminar el post
    if request.user != post.autor:
        return redirect('detalles_post', post_id=post.id) # Redirige al post si no es el autor
    
    if request.method == 'POST':
       post.delete()
       return redirect('lista_posts')
    return render(request, 'posts/eliminar_post.html', {'post': post})        