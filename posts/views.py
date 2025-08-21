from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/eliminar_post.html', {'post': post})

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalles_post', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/editar_post.html', {'form': form})

def detalles_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detalles_post.html', {'post': post})

@login_required
def nuevo_post(request):
    if request.method == 'POST':
        form =  PostForm(request.POST)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.autor = request.user
            nuevo_post.save()
            return redirect('Inicio')
    else:
        form = PostForm()
    return render(request, 'posts/nuevo_post.html', {'form': form})


def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')  # Los más nuevos primero
    return render(request, 'posts/lista_posts.html', {'posts': posts})