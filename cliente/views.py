from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Cliente, Telefone


def cadastro(request):
    return render(request, 'cliente/cadastro.html')


def cadastrar(request):
    if request.method == 'POST':
        # Captura dos dados do formulário
        email = request.POST["email"]
        senha = request.POST["senha"]
        numero_telefone = request.POST["numero_telefone"]
        # Pode ser "Sim" ou não definido
        whatsapp = request.POST.get("whatsapp", False)
        # Pode ser "Masculino" ou "Feminino"
        sexo = request.POST.get("genero", "")

        # Verifica se o usuário já existe
        if Cliente.objects.filter(email=email).exists():
            msg = "Erro: Este email já está cadastrado."
            return render(request, 'cliente/cadastro.html', {'msg': msg})

        telefone_obj, created = Telefone.objects.get_or_create(numero=numero_telefone)
        cliente = Cliente(email=email, senha_adicional=senha,
                          telefone=telefone_obj, whatsapp=whatsapp, sexo=sexo)

        try:
            cliente.save()
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
            cliente = Cliente.objects.get(email=email)
            if senha == cliente.senha_adicional:
                # Logar com sucesso
                # Você pode adicionar lógica de autenticação aqui
                print('logado')
                # Redirecionar para a página inicial ou outra página de destino
                return HttpResponseRedirect(reverse('pagina_inicial'))
            else:
                # Retornar senha incorreta
                msg = "Senha incorreta"
                return render(request, 'cliente/login.html', {'msg': msg})
        else:
            # Retornar usuário não cadastrado
            msg = "Usuário não encontrado"
            return render(request, 'cliente/login.html', {'msg': msg})
    else:
        # Se não for uma solicitação POST, renderizar a página de login
        return render(request, 'cliente/login.html')


def perfil(request):
    # A função de perfil requer que o usuário esteja autenticado
    return render(request, 'cliente/perfil.html')


def fazer_logout(request):
    logout(request)
    return redirect('cliente/login.html')
