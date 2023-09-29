from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', views.cadastro, name='registro'),
    path('registro/', views.cadastrar, name='cadastrar'),
    path('usuario/', views.perfil, name='usuario'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    
   
]
