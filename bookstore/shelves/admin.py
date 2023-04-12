"""
shelves admin
"""
from django.contrib import admin
from .models import Category,Book
# Register your models here.
admin.site.register(Category)

@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = 'category',