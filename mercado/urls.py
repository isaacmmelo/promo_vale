from django.urls import path
from . import views  # Importe as views da sua aplicação

urlpatterns = [
    # URLs da aplicação "mercado"
    path('mercado/', views.lista_mercado, name='lista_mercado'),
    path('mercado/<int:pk>/', views.detalhes_mercado, name='detalhes_mercado'),
    # Adicione mais URLs conforme necessário
]
