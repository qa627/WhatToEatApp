from django.db import models
from .ingredient import Ingredient

class IngredientDetail(models.Model):
    """食材詳細資訊（不常用的欄位）"""
    ingredient = models.OneToOneField(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='detail',
        verbose_name='食材'
    )
    origin = models.CharField(max_length=100, blank=True, verbose_name='產地')
    notes = models.TextField(blank=True, verbose_name='備註')
    storage_instructions = models.TextField(blank=True, verbose_name='儲存說明')

    class Meta:
        verbose_name = '食材詳細資料'
        verbose_name_plural = '食材詳細資料'

    def __str__(self):
        return f"{self.ingredient.name} 的詳細資料"
