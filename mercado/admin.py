from django.contrib import admin

# Register your models here.
from .models import Mercado

class MercadoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Mercado)