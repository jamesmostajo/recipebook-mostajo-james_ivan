from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipe_list': recipes}
    return render(request, "recipes_list.html", ctx)

def recipe(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    ctx = {
        "name": recipe.name,
        "ingredients": recipe.ingredients.all()
    }
    return render(request, "recipe.html", ctx)
