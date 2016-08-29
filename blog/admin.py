from django.contrib import admin
from .models import *
from django.db.models import Model
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',{'fields': ['title']}),
        ('Text',{"fields": ['text']}),
        ('Date',{"fields": ['pubdate','update']}),
        ('Author',{"fields": ['author']}),
        ('Category',{'fields': ['category']}),
        # ('Tag',{'fields': ['tags']})
    ]
    list_display = ['title','author','pubdate','update','text']
    list_filter = ['title','author','category']
    search_fields = ['title','author','category','update','pubdate']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categoty)
admin.site.register(Author)
admin.site.register(Comment)