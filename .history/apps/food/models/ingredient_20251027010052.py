from django.db import models
from .category import Category  # 匯入分類模型

class Ingredient(models.Model):
    """食材基本資訊"""
    name = models.CharField(max_length=100, verbose_name='食材名稱')
    quantity = models.IntegerField(default=0, verbose_name='數量')
    unit = models.CharField(max_length=20, verbose_name='單位', default='個')
    expiry_date = models.DateField(null=True, blank=True, verbose_name='到期日')
    storage_location = models.CharField(max_length=50, verbose_name='儲存位置', default='冷藏')

    # ForeignKey 建立一對多關聯（分類 → 食材）
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name='分類'
    )

    class Meta:
        verbose_name = '食材'
        verbose_name_plural = '食材管理'

    def __str__(self):
        return f"{self.name}（{self.quantity}{self.unit}）"
