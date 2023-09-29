from django.contrib import admin
from .models import Mercado

# Register your models here.
from .models import Mercado

class MercadoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["nome"]}),
        ( {"fields": ["pub_date"]}),
    ]




# ...
admin.site.register(Mercado)

