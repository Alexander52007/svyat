
from django.contrib import admin
from .models import Category, Product, Animal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['get_species_display', 'breed', 'age_months', 'gender', 'price', 'is_available']
    list_filter = ['species', 'is_available']
    search_fields = ['breed']