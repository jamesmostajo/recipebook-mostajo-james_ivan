from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField()
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredients', args=[str(self.pk)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        null=True,
        default = None,
        on_delete = models.CASCADE,
        related_name="users"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete =models.CASCADE,
        related_name = 'recipe'
    )

    recipe = models.ForeignKey(
        'Recipe',
        on_delete =models.CASCADE,
        related_name = 'ingredients'
    )

    # for debugging
    def __str__(self):
        return f'{self.quantity} of {self.ingredient} for {self.recipe}'

