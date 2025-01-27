from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Cambia a la página que desees redirigir después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'gob/login.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('/login/')  # Redirige a la página de login después de cerrar sesión

# Vista del aviso de privacidad
def aviso_privacidad_view(request):
    return render(request, 'gob/aviso_privacidad.html')
