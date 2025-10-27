# apps/food/views.py
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Ingredient, Category

# 首頁
class IndexView(View):
    def get(self, request):
        # 可以顯示所有食材列表或熱門食材
        ingredients = Ingredient.objects.all()
        return render(request, 'food/index.html', {'ingredients': ingredients})

# 食材列表
class IngredientListView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        ingredients = Ingredient.objects.all()
        if query:
            ingredients = ingredients.filter(name__icontains=query)
        return render(request, 'food/ingredient_list.html', {'ingredients': ingredients})

# 食材詳細
class IngredientDetailView(View):
    def get(self, request, ingredient_id):
        ingredient = get_object_or_404(Ingredient, id=ingredient_id)
        return render(request, 'food/ingredient_detail.html', {'ingredient': ingredient})
    
# 分類列表
class CategoryListView(View):
    """分類列表"""
    def get(self, request):
        categories = Category.objects.all()  # 等你有 Category 模型
        return render(request, 'food/category_list.html', {'categories': categories})

class CategoryDetailView(View):
    """分類詳細"""
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        return render(request, 'food/category_detail.html', {'category': category})

# function-based view
def category_ingredients(request, category_id):
    category = Category.objects.get(id=category_id)
    ingredients = category.ingredients.all()  # 假設 Ingredient 有 ManyToMany 或 ForeignKey
    return render(request, 'food/category_ingredients.html', {'category': category, 'ingredients': ingredients})
