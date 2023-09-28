from django.urls import path
from . import views  # Importe as views da sua aplicação

urlpatterns = [
    # Exemplo de URLs da aplicação "contatos"
    path('lista-contatos/', views.lista_contatos, name='lista_contatos'),
    path('contato/<int:pk>/', views.detalhes_contato, name='detalhes_contato'),
        
    # Adicione mais URLs conforme necessário
]
