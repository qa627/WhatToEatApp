from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # 首頁
    path('', views.index, name='index'),

    # 食材列表與詳細頁
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),

    # 分類相關
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:category_id>/ingredients/', views.category_ingredients, name='category_ingredients'),
]
