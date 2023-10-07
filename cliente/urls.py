from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('registro/', views.cadastro, name='registro'),
    path('registrar/', views.cadastrar, name='registrar'),
    path('perfil/', views.perfil, name='perfil'),    
    path('login/', views.fazer_login, name='login'),
    #path('fazer_login/', views.fazer_login, name='fazer_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]
urlpatterns += staticfiles_urlpatterns()
