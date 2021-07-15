import requests
from decouple import config as secret


class SpoonacularApiServiceError(Exception):
    """
    Handle error in PreciselyApiService.
    """


class SpoonacularApiService:
    def __init__(self):
        self._base_url = "https://api.spoonacular.com/recipes"
        self._session = requests.session()

    def _get(self, endpoint, params=None):
        headers = {"content-type": "application/json"}
        response = self._session.get(f"{self._base_url}/{endpoint}", params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def _get_by_ingredients(self, ingredients: str):
        endpoint = "findByIngredients"
        params = {}
        ingredients_quantity = len(ingredients.split(", ")) if "," in ingredients else 0
        try:
            if ingredients_quantity <= 3 and ingredients_quantity != 0:
                params["apiKey"] = self._get_api_key()
                params["ingredients"] = ingredients
                result = self._get(endpoint, params=params)
                return self._handle_data(result)
            else:
                message = f"Should get 1 to 3 ingredients but got {ingredients_quantity}"
                raise SpoonacularApiServiceError(message)
        except Exception as error:
            message = f"Error getting endpoint {endpoint} with params {ingredients}: {error}"
            raise SpoonacularApiServiceError(message)

    def _handle_data(self, response):
        handle_recipes = []
        dict_recipe = {}
        for recipe in response:
            dict_recipe["title"] = recipe["title"]
            dict_recipe["image"] = recipe["image"]
            dict_recipe["ingredient"] = [ingredient["name"] for ingredient in recipe["usedIngredients"]]
            dict_recipe["ingredient"] += [ingredient["name"] for ingredient in recipe["missedIngredients"]]
            handle_recipes.append(dict_recipe)
            return handle_recipes

    def _get_api_key(self):
        return secret("API_KEY")
