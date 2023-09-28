from django.urls import path
from . import views  # Importe as views do aplicativo

app_name = 'stories'  # Opcional: Nome do aplicativo para evitar conflitos de URL com outros aplicativos

urlpatterns = [
    path('lista/', views.lista_stories, name='lista_stories'),
    path('detalhes/<int:pk>/', views.detalhes_stories, name='detalhes_stories'),
    # Adicione mais URLs conforme necessário para as funcionalidades do aplicativo de stories
]