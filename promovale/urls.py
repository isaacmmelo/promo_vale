from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('promocao/', include('promocao.urls')),
    path('mercado/', include('mercado.urls')),
    path('stories/', include('stories.urls')),    
]

