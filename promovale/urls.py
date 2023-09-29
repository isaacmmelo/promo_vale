from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('promocao/', include('promocao.urls')),
    path('mercado/', include('mercado.urls')),
    path('stories/', include('stories.urls')),
    path('contatos/', include('contatos.urls')),
    
    
]

