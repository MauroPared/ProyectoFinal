# paginas/views.py


from django.shortcuts import render
from posts.models import Post  # Importar desde la app de posts

def Inicio(request):
    posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    return render(request, 'paginas/home.html', {'posts': posts})

def Acerca_De(request):
    return render(request, 'paginas/acerca_de.html')

def Contacto(request):
    return render(request, 'paginas/contacto.html')

