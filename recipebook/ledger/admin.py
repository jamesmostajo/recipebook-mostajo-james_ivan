from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.

class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientAdmin]  

admin.site.register(Recipe, RecipeAdmin)