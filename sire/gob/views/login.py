from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Por favor, introduce ambos campos.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Cambia a la página que desees redirigir después de iniciar sesión
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'gob/login.html')


def logout_view(request):
    logout(request)
    return redirect('/gob/login/')  # Redirige a la página de login después de cerrar sesión

def aviso_privacidad_view(request):
    return render(request, 'gob/aviso_privacidad.html')
