from django.contrib import admin

from .models import RecipeIngredient, Recipe, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_used')
    search_fields = ('name',)
    list_filter = ('times_used',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Product, ProductAdmin)
