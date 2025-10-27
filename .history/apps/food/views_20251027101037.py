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
