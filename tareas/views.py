from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def Inicio(request):
    posts = Post.objects.all().order_by('-fecha_creacion')[:5]  # Los 5 primeros post se muestran
    return render(request, 'tareas/home.html', {'posts': posts})

def Acerca_De(request):
    return render(request, 'tareas/acerca_de.html')

def Contacto(request):
    return render(request, 'tareas/contacto.html')

def Registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect('Blog-Inicio')
    else:
        form = UserCreationForm()
    return render(request, 'tareas/registro.html', {'form': form})

def Loguearse(request):
    return render(request, 'tareas/login.html')

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'tareas/eliminar_post.html', {'post': post})

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
    return render(request, 'tareas/editar_post.html', {'form': form})

def detalles_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'tareas/detalles_post.html', {'post': post})

@login_required
def nuevo_post(request):
    if request.method == 'POST':
        form =  PostForm(request.POST)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.autor = request.user
            nuevo_post.save()
            return redirect('Blog-Inicio')
    else:
        form = PostForm()
    return render(request, 'tareas/nuevo_post.html', {'form': form})

def categorias(request):
    return render(request, 'tareas/categorias.html')

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')  # Los más nuevos primero
    return render(request, 'tareas/lista_posts.html', {'posts': posts})