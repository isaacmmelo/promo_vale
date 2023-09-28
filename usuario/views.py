from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm

def configuracoes(request):
    # Sua lógica para a view de configurações aqui
    return render(request, 'usuario/configuracoes.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro realizado com sucesso!')
            # Redirecionar para o perfil do usuário após o registro
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'usuario/registro.html', {'form': form})

def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, email=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('perfil')
            else:
                messages.error(
                    request, 'Credenciais inválidas. Por favor, tente novamente.')
    else:
        form = LoginForm()
    return render(request, 'usuario/login.html', {'form': form})

@login_required
def perfil(request):
    user = request.user
    return render(request, 'usuario/perfil.html', {'user': user})
