from django.shortcuts import render

def promocoes(request):
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
    return render(request, 'cliente/promocoes.html', {'promocoes': promocoes})
