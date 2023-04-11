"""
shelves admin
"""
from django.contrib import admin
from .models import Category,Books
# Register your models here.
admin.site.register(Category)

@admin.register(Books)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = 'category',