from django.contrib import admin
from .models import Stories

class StoriesAdmin(admin.ModelAdmin):
    fields = ["data_publicacao"]


admin.site.register(Stories, StoriesAdmin)
