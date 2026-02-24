from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    search_fields = ("title", "body")
    list_filter = ("date", "author")
    
admin.site.register(Article, ArticleAdmin)
