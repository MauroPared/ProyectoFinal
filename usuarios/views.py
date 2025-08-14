from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def Registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Inicia sesión automáticamente
            return redirect('Blog-Inicio')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def Loguearse(request):
    return render(request, 'usuarios/login.html')