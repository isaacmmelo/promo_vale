from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Cliente

def cadastro(request):
    return render(request, 'cliente/cadastro.html')

def cadastrar(request):
    if request.method == 'POST':
        # Captura dos dados do formulário
        email = request.POST["email"]
        senha = request.POST["senha"]
        telefone = request.POST["telefone"]
        whatsapp = request.POST.get("whatsapp", False)  # Pode ser "Sim" ou não definido
        sexo = request.POST.get("genero", "")  # Pode ser "Masculino" ou "Feminino"

        # Verifica se o usuário já existe
        if Cliente.objects.filter(email=email).exists():
            msg = "Erro: Este email já está cadastrado."
            return render(request, 'cliente/cadastro.html', {'msg': msg})
        
        cliente = Cliente
        cliente.email = email
        cliente.senha_adicional = senha
        cliente.telefone = telefone
        cliente.whatsapp = whatsapp
        cliente.sexo = sexo

        try:
            resultado = cliente.save()
        except:
            msg = "Erro no cadastro, tente novamente"
            return render(request, 'cliente/cadastro.html', {'msg': msg}) 
        else:
            msg = "Cadastro realizado com sucesso! Faça o login"
            return render(request, 'cliente/login.html', {'msg': msg}) 

def fazer_login(request):
    if request.method == 'POST':
        # Processar os dados do formulário de login aqui
        email = request.POST['email']
        senha = request.POST['senha']
               
        if Cliente.objects.filter(email=email).exists():
            cliente = Cliente.get(email=email)
            if (senha == cliente.senha):
                #logar
                print('logado')
                #redirecion para a página inicial
            else:
                #retornar senha incorreta
                msg = "Senha incorreta"
                return render(request, 'cliente/login.html', {'msg': msg})
        else:
            #retornar usuario não cadastrado
            msg = "Usuario não encontrado"
            return render(request, 'cliente/login.html', {'msg': msg}) 

def perfil(request):
    # A função de perfil requer que o usuário esteja autenticado
    return render(request, 'cliente/perfil.html')

def fazer_logout(request):
    logout(request)
    return redirect('cliente/login.html')
