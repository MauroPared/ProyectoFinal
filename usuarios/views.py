from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from posts.models import Post

def Registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente
            return redirect('Inicio')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    
    ultimos_posts = Post.objects.filter(autor=request.user).order_by('-fecha_creacion')[:5]
    return render(request, 'usuarios/perfil.html', {'ultimos_posts': ultimos_posts})


