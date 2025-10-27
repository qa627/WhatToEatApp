from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # 首頁
    path('', views.IndexView.as_view(), name='index'),

    # Ingredient
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:ingredient_id>/', views.IngredientDetailView.as_view(), name='ingredient_detail'),
    path('ingredients/search/', views.IngredientSearchView.as_view(), name='ingredient_search'),
    path('ingredients/filter/', views.IngredientFilterView.as_view(), name='ingredient_filter'),

    # Category
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:category_id>/ingredients/', views.category_ingredients, name='category_ingredients'),

    # Recipe
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]
