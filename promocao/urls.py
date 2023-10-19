# No arquivo promocao/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.promocoes, name='promocoes')
]