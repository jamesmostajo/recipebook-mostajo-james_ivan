from django.urls import path

from .views import recipe, recipes_list

urlpatterns = [
    path("recipes/list", recipes_list, name="recipes_list"),
    path("recipe/<int:pk>/", recipe, name="recipe_detail"),
]

app_name = "ledger"
