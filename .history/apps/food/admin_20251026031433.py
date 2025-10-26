from django.contrib import admin
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    # 列表頁面顯示欄位
    list_display = ('name', 'quantity', 'unit', 'category', 'storage_location', 'expiry_date')
    
    # 右側篩選器
    list_filter = ('category', 'storage_location')
    
    # 搜尋欄位
    search_fields = ('name', 'category')
    
    # 預設排序
    ordering = ('-expiry_date', 'name')  # 先依到期日降冪，再依名稱升冪
