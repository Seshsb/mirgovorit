from django.db import transaction
from django.db.models import Q, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from .models import RecipeIngredient, Recipe, Product


@transaction.atomic
def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    if recipe_id and product_id and weight:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        recipe_ingredient, created = RecipeIngredient.objects.update_or_create(
            recipe=recipe, product=product,
            defaults={'weight': weight})
        return redirect('recipe_detail', recipe_id=recipe_id)
    return HttpResponse("Invalid parameters provided.")


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    result = {
        'recipe_data': {
            'id': recipe.id,
            'name': recipe.name,
            'ingredients': [{'product_id': ingredient.product.id,
                             'weight': ingredient.weight} for ingredient in recipe.recipe_ingredients.all()]
        }
    }

    return JsonResponse(result)


@transaction.atomic
def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        products_ids = recipe.recipe_ingredients.values_list('product', flat=True)
        products = get_list_or_404(Product, pk__in=products_ids)

        Product.objects.filter(pk__in=products_ids).update(times_used=F('times_used') + 1)
        return JsonResponse(data={'result': 'Successful'}, status=200)
    return HttpResponse("Invalid parameters provided.")


@transaction.atomic
def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    if product_id:
        product = get_object_or_404(Product, pk=product_id)
        recipes = (Recipe.objects.exclude(recipe_ingredients__product=product) |
                   Recipe.objects.filter(recipe_ingredients__product=product, recipe_ingredients__weight__lt=10))
        context = {'product': product, 'recipes': recipes}

        return render(request, 'cookbook/show_recipes_without_product.html', context)
    return HttpResponse('Invalid parameters provided.')
