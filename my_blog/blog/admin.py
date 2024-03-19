from django.contrib import admin
from .models import Rating,Author,Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_filter=("author","rating","date")
    list_display = ("title","date","author")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Article,ArticleAdmin)
admin.site.register(Rating)
admin.site.register(Author)