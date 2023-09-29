from django.shortcuts import render

# Create your views here.
def cadastro(request):
    return render(request, 'usuario/cadastro.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def cadastrar(request):
    if request.method == 'POST':
        # Captura dos dados do formulário
        email = request.POST["email"]
        senha = request.POST["senha"]
        telefone = request.POST["telefone"]
        whatsapp = request.POST.get("whatsapp", False)  # Pode ser "Sim" ou não definido
        sexo = request.POST.get("genero", "")  # Pode ser "Masculino" ou "Feminino"

        # Criação de um novo usuário
        usuario = User.objects.create_user(username=email, password=senha)

        # Salvar informações adicionais no perfil do usuário
        usuario.userprofile.telefone = telefone
        usuario.userprofile.whatsapp = whatsapp == "Sim"
        usuario.userprofile.sexo = sexo
                
        try:
            usuario.userprofile.save()
        except:
            msg = "Erro no cadastro"
            return redirect('usuario/cadastro.html') 
        else:
            msg = "Cadastro realizado com sucesso"
            return render(request, 'usuario/login.html',msg) 
 

def fazer_login(request):
    if request.method == 'POST':
        # Processar os dados do formulário de login aqui
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
    elif request.method == 'GET' and request.user.is_authenticated:
        # Se o usuário já estiver autenticado e acessar a página de login,
        # redirecioná-lo para a página de perfil ou outra página apropriada.
        return redirect('perfil')
    return render(request, 'fazer_login.html')

def perfil(request):
    # A função de perfil requer que o usuário esteja autenticado
    return render(request, 'perfil.html')

def fazer_logout(request):
    logout(request)
    return redirect('login')
