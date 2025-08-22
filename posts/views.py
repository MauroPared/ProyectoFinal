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
        'form': form_comentario,
    })


@login_required
def nuevo_post(request):
    # Verificación: si el usuario no es moderador, lo redirige
    if not request.user.is_staff:
        return redirect('lista_posts') #solo moderadores
    
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

    # Solo moderadores (staff) pueden editar
    if not request.user.is_staff:
        return redirect('detalles_post', post_id=post.id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalles_post', post_id=post.id)
    else:
        form = PostForm(instance=post)  # 🔹 IMPORTANTE: siempre inicializar form en GET

    return render(request, 'posts/editar_post.html', {'form': form, 'post': post})

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    #El autor puede eliminar el post
    if not request.user.is_staff:
        return redirect('detalles_post', post_id=post.id) # Redirige al post si no es el moderador
    if request.method == 'POST':
       post.delete()
       return redirect('lista_posts')
    return render(request, 'posts/eliminar_post.html', {'post': post}) 



from django.shortcuts import render
from .models import Post, Categoria

def lista_posts(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()

    # --- FILTROS ---
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        posts = posts.filter(categoria_id=categoria_id)

    # --- ORDEN ---
    orden = request.GET.get('orden')
    if orden == 'antiguedad_asc':
        posts = posts.order_by('fecha_creacion')   # más antiguos primero
    elif orden == 'antiguedad_desc':
        posts = posts.order_by('-fecha_creacion')  # más nuevos primero
    elif orden == 'alfabetico_asc':
        posts = posts.order_by('titulo')
    elif orden == 'alfabetico_desc':
        posts = posts.order_by('-titulo')

    return render(request, 'posts/lista_posts.html', {
        'posts': posts,
        'categorias': categorias,
    })       