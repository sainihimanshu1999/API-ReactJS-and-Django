from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Article

#admin.site.register(Article)

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title','description')
    list_display = ('title','description')

# Register your models here.


