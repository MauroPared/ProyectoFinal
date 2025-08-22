# paginas/views.py
from .models import Mensaje
from django.shortcuts import render, redirect
from posts.models import Post  # Importar desde la app de posts
from .forms import ContactoForm

def Inicio(request):
    posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    return render(request, 'paginas/home.html', {'posts': posts})

def Acerca_De(request):
    return render(request, 'paginas/acerca_de.html')

def Contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            #Guarda el mensaje en base de datos
            Mensaje.objects.create(
                nombre=nombre,
                email=email,
                mensaje=mensaje
            )

            return redirect('Inicio')
    else:
        form = ContactoForm()

    return render(request, 'paginas/contacto.html', {'form': form})

