from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Contato

def lista_contatos(request):
    # Lógica para recuperar os contatos aqui
    return render(request, 'storys/lista_contatos.html')

def detalhes_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    return render(request, 'contatos/detalhes_contato.html', {'contato': contato})
