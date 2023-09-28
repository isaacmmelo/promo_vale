from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('usuario/', views.perfil, name='usuario'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('registro/', views.registro, name='registro'),
    
    # Adicione mais URLs conforme necessário
]
