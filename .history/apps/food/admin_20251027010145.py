from django.contrib import admin
from .models import Category, Ingredient, IngredientDetail

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'category', 'storage_location', 'expiry_date')
    list_filter = ('category', 'storage_location')
    search_fields = ('name',)
    ordering = ('-expiry_date', 'name')


@admin.register(IngredientDetail)
class IngredientDetailAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'origin')
    search_fields = ('ingredient__name', 'origin')
    ordering = ('ingredient__name',)
