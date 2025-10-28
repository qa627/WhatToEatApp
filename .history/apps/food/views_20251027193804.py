from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Ingredient, Category

# 首頁
class IndexView(View):
    def get(self, request):
        # 顯示所有食材列表或熱門食材
        ingredients = Ingredient.objects.all()
        # 可透過查詢參數排序
        order_by = request.GET.get('order', 'id')
        ingredients = ingredients.order_by(order_by)
        # 搜尋
        query = request.GET.get('q', '')
        if query:
            ingredients = ingredients.filter(name__icontains=query)

        return render(request, 'food/index.html', {'ingredients': ingredients})

# 食材列表
class IngredientListView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        ingredients = Ingredient.objects.all()
        
        # 搜尋
        if query:
            ingredients = ingredients.filter(name__icontains=query)
        
        # 排序
        order_by = request.GET.get('order', 'id')
        ingredients = ingredients.order_by(order_by)
        
        # 篩選數量
        min_qty = request.GET.get('min_qty')
        max_qty = request.GET.get('max_qty')
        if min_qty:
            ingredients = ingredients.filter(quantity__gte=int(min_qty))
        if max_qty:
            ingredients = ingredients.filter(quantity__lte=int(max_qty))
        
        return render(request, 'food/ingredient_list.html', {'ingredients': ingredients})

# 食材詳細
class IngredientDetailView(View):
    def get(self, request, ingredient_id):
        ingredient = get_object_or_404(Ingredient, id=ingredient_id)
        
        # 顯示相關食材（同分類）
        show_related = request.GET.get('show_related', 'no')
        related = []
        if show_related == 'yes' and ingredient.category:
            related = Ingredient.objects.filter(category=ingredient.category).exclude(id=ingredient.id)[:3]
        
        return render(request, 'food/ingredient_detail.html', {
            'ingredient': ingredient,
            'related': related
        })

# 分類列表
class CategoryListView(View):
    """分類列表"""
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'food/category_list.html', {'categories': categories})

# 分類詳細
class CategoryDetailView(View):
    """分類詳細"""
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        return render(request, 'food/category_detail.html', {'category': category})

# 分類下的食材
def category_ingredients(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ingredients = category.ingredients.all()  # 假設 Ingredient 有 ManyToMany 或 ForeignKey
    
    # 查詢參數篩選
    query = request.GET.get('q', '')
    if query:
        ingredients = ingredients.filter(name__icontains=query)
    
    order_by = request.GET.get('order', 'id')
    ingredients = ingredients.order_by(order_by)
    
    return render(request, 'food/category_ingredients.html', {
        'category': category,
        'ingredients': ingredients
    })
