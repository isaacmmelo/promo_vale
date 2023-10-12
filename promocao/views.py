from django.shortcuts import render,get_object_or_404
from .models import Promocao
from mercado.models import Mercado

""" def promocoes(request):
    #Pegar os dados de usuário da sessão

    # Lógica para obter promoções do banco de dados ou de outra fonte de dados
    promocoes = [
        {
            'titulo': 'Promoção de Verão',
            'descricao': 'Descontos incríveis para você aproveitar o verão!',
            'data_inicio': '2023-06-01',
            'data_fim': '2023-08-31',
        },
        {
            'titulo': 'Promoção de Inverno',
            'descricao': 'Fique aquecido com descontos exclusivos!',
            'data_inicio': '2023-12-01',
            'data_fim': '2024-02-29',
        },
        # Adicione mais promoções conforme necessário
    ]

    # Renderiza a página de promoções e passa a lista de promoções para o template
    return render(request, 'promocao/index.html', {'promocoes': promocoes}) """

def promocoes(request):
    promocoes_todas = Promocao.objects
    mercado_todos = Mercado.objects
    
    saida={"lista_promocao": promocoes_todas.all, "lista_mercado": mercado_todos}
    return render (request, 'promocao/index.html', saida)

    
   
    
