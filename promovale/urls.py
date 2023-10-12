from django.contrib import admin
from django.urls import include, re_path, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls import *
from django.views.static import serve


urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('promocao/', include('promocao.urls')),
    path('mercado/', include('mercado.urls')),
    path('stories/', include('stories.urls')),   
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), 
]