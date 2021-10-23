from django.contrib import admin
from async_project.models import Registerdb, Article

@admin.register(Registerdb)
class RegisterdbAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
