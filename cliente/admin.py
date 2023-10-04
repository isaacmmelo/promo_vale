from django.contrib import admin
from .models import Cliente

# Register your models here.
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["nome"]}),
        ( {"fields": ["pub_date"]}),
    ]




# ...
admin.site.register(Cliente)

# Register your models here.
