from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","slug"]
    search_fields = ["title"]
    readonly_fields =["slug"]

admin.site.register(Blog,BlogAdmin)
