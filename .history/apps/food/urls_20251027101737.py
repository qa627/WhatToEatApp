from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # 首頁
    path('', views.IndexView.as_view(), name='index'),

    # 食材列表與詳細頁
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:ingredient_id>/', views.IngredientDetailView.as_view(), name='ingredient_detail'),

    # 分類相關
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:category_id>/ingredients/', views.category_ingredients, name='category_ingredients'),
]
