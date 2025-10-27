from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Ingredient, Category, Recipe

# --------- Index ----------
class IndexView(View):
    def get(self, request):
        return render(request, 'food/index.html')


# --------- Ingredient ----------
class IngredientListView(View):
    """食材列表，可排序"""
    def get(self, request):
        order_by = request.GET.get('order', 'id')
        ingredients = Ingredient.objects.order_by(order_by)
        context = {'ingredients': ingredients, 'order_by': order_by}
        return render(request, 'food/ingredient_list.html', context)

class IngredientDetailView(View):
    """食材詳細頁 + 相關食材推薦"""
    def get(self, request, ingredient_id):
        ingredient = get_object_or_404(Ingredient, id=ingredient_id)
        show_related = request.GET.get('show_related', 'no')
        related = None
        if show_related == 'yes' and ingredient.category:
            related = Ingredient.objects.filter(category=ingredient.category)\
                        .exclude(id=ingredient.id)[:3]
        context = {
            'ingredient': ingredient,
            'related': related
        }
        return render(request, 'food/ingredient_detail.html', context)

class IngredientSearchView(View):
    """食材搜尋"""
    def get(self, request):
        query = request.GET.get('q', '')
        ingredients = Ingredient.objects.filter(name__icontains=query) if query else []
        context = {'ingredients': ingredients, 'query': query}
        return render(request, 'food/ingredient_search.html', context)

class IngredientFilterView(View):
    """食材篩選"""
    def get(self, request):
        min_qty = request.GET.get('min_qty')
        max_qty = request.GET.get('max_qty')
        ingredients = Ingredient.objects.all()
        if min_qty:
            ingredients = ingredients.filter(quantity__gte=int(min_qty))
        if max_qty:
            ingredients = ingredients.filter(quantity__lte=int(max_qty))
        context = {'ingredients': ingredients, 'min_qty': min_qty, 'max_qty': max_qty}
        return render(request, 'food/ingredient_filter.html', context)


# --------- Category ----------
class CategoryListView(View):
    """分類列表"""
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'food/category_list.html', {'categories': categories})

class CategoryDetailView(View):
    """分類詳細"""
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        ingredients = category.ingredient_set.all()
        return render(request, 'food/category_detail.html', {
            'category': category,
            'ingredients': ingredients
        })

def category_ingredients(request, category_id):
    """用 function view 也可以做分類食材列表"""
    category = get_object_or_404(Category, id=category_id)
    ingredients = category.ingredient_set.all()
    return render(request, 'food/category_ingredients.html', {
        'category': category,
        'ingredients': ingredients
    })


# --------- Recipe ----------
class RecipeListView(View):
    """食譜列表"""
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'food/recipe_list.html', {'recipes': recipes})

class RecipeDetailView(View):
    """食譜詳細"""
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        return render(request, 'food/recipe_detail.html', {'recipe': recipe})
