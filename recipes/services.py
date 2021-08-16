import requests
from decouple import config as secret
from requests import Response


class SpoonacularApiServiceError(Exception):
    """
    Handle error in SpoonacularApiService.
    """


class SpoonacularApiService(object):
    """
    Class for making requests to Spoonacular Api.
    """

    def __init__(self):
        self._base_url = "https://api.spoonacular.com/recipes"
        self._session = requests.session()

    def _get(self, endpoint, params=None) -> Response:
        headers = {"content-type": "application/json"}
        response = self._session.get(
            f"{self._base_url}/{endpoint}", params=params, headers=headers
        )
        response.raise_for_status()
        return response

    def get_by_ingredients(self, ingredients: str) -> list:
        """
        Method to get recipes by ingredients name.
        Maximum of 3 ingredients allowed.

        Args:
            - ingredients (str): it's sent as query param from our api.
        """
        endpoint = "findByIngredients"
        params = {}
        ingredients_quantity = 0
        if ingredients:
            ingredients_quantity = (
                len(ingredients.split(",")) if "," in ingredients else 1
            )
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

    @staticmethod
    def _handle_data(response) -> list:
        """
        It's used to manipulate the Spoonacular API response to return the following attributes:
        - title;
        - image;
        - ingredients.

        Args:
            - response (Response): It's received from _get method.
        """
        handle_recipes = []
        for recipe in response.json():
            dict_recipe = {
                "title": recipe["title"],
                "image": recipe["image"],
                "ingredients": [
                    ingredient["name"]
                    for ingredient in recipe["usedIngredients"]
                ],
            }
            dict_recipe["ingredients"] += [
                ingredient["name"]
                for ingredient in recipe["missedIngredients"]
            ]
            handle_recipes.append(dict_recipe)
        return handle_recipes

    @staticmethod
    def _get_api_key() -> str:
        """
        Get the API_KEY from .env file
        """
        return secret("API_KEY")
