from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipe_list": recipes}
    return render(request, "recipes_list.html", ctx)


@login_required
def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        "name": recipe.name,
        "author": recipe.author,
        "ingredients": recipe.ingredients.all(),
        "created_on": recipe.created_on,
        "updated_on": recipe.updated_on,
    }
    return render(request, "recipe_detail.html", ctx)
