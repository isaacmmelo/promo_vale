from django.shortcuts import render,get_object_or_404
from .models import Promocao
from mercado.models import Mercado

def promocoes(request):
    promocoes_todas = Promocao.objects
    mercado_todos = Mercado.objects
    
    saida={"lista_promocao": promocoes_todas.all, "lista_mercado": mercado_todos.all}
    return render (request, 'promocao/index.html', saida)

    
   
    
