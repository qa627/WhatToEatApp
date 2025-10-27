from django.db import models

class Category(models.Model):
    """食材分類"""
    name = models.CharField(max_length=50, verbose_name='分類名稱')
    description = models.TextField(blank=True, null=True, verbose_name='描述')

    class Meta:
        verbose_name = '食材分類'
        verbose_name_plural = '食材分類'

    def __str__(self):
        return self.name
