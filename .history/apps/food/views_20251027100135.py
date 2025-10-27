
from django.views import View
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient, Category

# 首頁
class IndexView(View):
    def get(self, request):
        return render(request, 'food/index.html')

# 食譜列表
class RecipeListView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        recipes = Recipe.objects.all()
        if query:
            recipes = recipes.filter(name__icontains=query)
        return render(request, 'food/recipe_list.html', {'recipes': recipes})

# 食譜詳細
class RecipeDetailView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        return render(request, 'food/recipe_detail.html', {'recipe': recipe})

# 類別列表
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'food/category_list.html', {'categories': categories})

# 類別詳細（顯示該類別下的食譜）
class CategoryDetailView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        recipes = category.recipes.all()  # 假設 Recipe 有 ManyToManyField to Category
        return render(request, 'food/category_detail.html', {'category': category, 'recipes': recipes})

