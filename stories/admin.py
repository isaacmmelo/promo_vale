from django.contrib import admin
from .models import Stories

class StoriesAdmin(admin.StoriesAdmin):
    fields = ["pub_data", "stories_texto"]


admin.site.register(Stories, StoriesAdmin)
