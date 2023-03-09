from django.db import models


# Create your models here.
class Category(models.Model):
    name_cat = models.CharField(max_length=50, verbose_name='Nome da categoria')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name_cat
