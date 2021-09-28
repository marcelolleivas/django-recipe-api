import httpretty as httpretty
import pytest


@pytest.fixture
def disable_external_api_calls():
    httpretty.disable()


@pytest.fixture
def client():
    from django.test.client import Client

    return Client()


@pytest.fixture
def ingredient_return():
    return [
        {
            "title": "Charred spring onions",
            "image": "https://spoonacular.com/recipeImages/1089425-312x231.jpg",
            "ingredients": ["spring onions"],
        }
    ]


@pytest.fixture
def spoonacular_ingredient_response():
    return [
        {
            "id": 1089425,
            "title": "Charred spring onions",
            "image": "https://spoonacular.com/recipeImages/1089425-312x231.jpg",
            "imageType": "jpg",
            "usedIngredientCount": 1,
            "missedIngredientCount": 0,
            "missedIngredients": [],
            "usedIngredients": [
                {
                    "id": 11291,
                    "amount": 2.0,
                    "unit": "bunches",
                    "unitLong": "bunches",
                    "unitShort": "bunches",
                    "aisle": "Produce",
                    "name": "spring onions",
                    "original": "2 bunches of spring onions (about 20)",
                    "originalString": "2 bunches of spring onions (about 20)",
                    "originalName": "spring onions (about 20)",
                    "metaInformation": ["( 20)"],
                    "meta": ["( 20)"],
                    "image": "https://spoonacular.com/cdn/ingredients_100x100/spring-onions.jpg",
                }
            ],
            "unusedIngredients": [],
            "likes": 1,
        }
    ]
