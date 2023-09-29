from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', views.cadastro, name='registro'),
    path('registrar/', views.cadastrar, name='registrar'),
    path('cliente/', views.perfil, name='cliente'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
