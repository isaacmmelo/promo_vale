from django.contrib import admin
from .models import Cliente, Telefone

class TelefoneInline(admin.StackedInline):
    model = Telefone
    extra = 1

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["nome"]}),
        ( {"fields": ["email"]}),
    ]
    inlines = [TelefoneInline]

# ...
admin.site.register(Cliente)

# Register your models here.
