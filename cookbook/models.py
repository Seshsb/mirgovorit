from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование', unique=True)
    times_used = models.IntegerField(default=0, verbose_name='Количество использования')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    ingredients = models.ManyToManyField(Product, verbose_name='Ингридиенты', through='RecipeIngredient',
                                         related_name='ingredients')

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, verbose_name='Рецепт', on_delete=models.CASCADE,
                               related_name='recipe_ingredients',
                               related_query_name='recipe_ingredients')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE,
                                related_name='product_ingredients',
                                related_query_name='product_ingredients')
    weight = models.IntegerField(verbose_name='Вес')

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name}"
