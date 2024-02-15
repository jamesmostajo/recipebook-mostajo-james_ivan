from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def recipes_list(request):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3 pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1 pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1 L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1 pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2 cup"
                    },
                    {
                        "name": "water",
                        "quantity": "1 cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "/recipe/2"
            }
        ]
    }
    return render(request, "recipes_list.html", ctx)

def recipe_1(request):
    ctx = {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3 pcs"
            },
            {
                "name": "onion",
                "quantity": "1 pc"
            },
            {
                "name": "pork",
                "quantity": "1 kg"
            },
            {
                "name": "water",
                "quantity": "1 L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "/recipe/1"
    }
    return render(request, "recipe_1.html", ctx)

def recipe_2(request):
    ctx = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1 pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2 cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
    return render(request, "recipe_2.html", ctx)
