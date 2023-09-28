# No arquivo promocao/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('promocoes/', views.promocoes, name='promocoes')
]
