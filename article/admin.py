from django.contrib import admin

from .models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['uuid', 'title', 'created_at', 'updated_at']
    list_display = ['uuid', 'title', 'created_at', 'updated_at']