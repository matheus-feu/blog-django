from django.contrib import admin
from .models import Category


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat',)
    list_display_links = ('id', 'name_cat')
    search_fields = ('name_cat',)


admin.site.register(Category, CategoriaAdmin)
