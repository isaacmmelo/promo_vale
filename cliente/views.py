from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Cliente, Telefone
## https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Sessions

def cadastro(request):
    return render(request, 'cliente/cadastro.html')


def cadastrar(request):
    if request.method == 'POST':
        # Captura dos dados do formulário
        nome = request.POST["nome"]
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
        cliente = Cliente(nome=nome, email=email, senha_adicional=senha,
                          telefone=telefone_obj, whatsapp=whatsapp, sexo=sexo)

        try:
            resultado = cliente.save()
            print('resultado: ',resultado)
        except Exception as error:
            print('resultado com erro: ',error)
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
                request.session['user_name'] = cliente.nome
                request.session['user_email'] = cliente.email
                request.session['user_id'] = cliente.pk

                # Redirecionar para a página inicial ou outra página de destino
                #return render(request, '/promocao/index.html', {'cliente': cliente})
                return redirect('/promocao/')
                
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
