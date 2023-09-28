from django.shortcuts import render
from django.http import HttpResponse
from .models import Mercado  # Importe o modelo de Mercado 

def detalhes_mercado(request, pk):
    # Recupere o mercado com base na chave primária (pk) 
    mercado = Mercado.objects.get(pk=pk)
    return render(request, 'mercado/detalhes_mercado.html', {'mercado': mercado})

def lista_mercado(request):
    mercado = Mercado.objects.all()  # Corrija o nome da variável para 'mercados'
    return render(request, 'mercado/lista_mercado.html', {'mercado': mercado})
