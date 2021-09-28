import os
import sys

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe_factory.settings")


@pytest.mark.parametrize(
    "query_param",
    [
        "onions",
        "onions,tomatoes",
        "onions,tomatoes,eggs",
    ],
)
@pytest.mark.django_db
def test_should_return_recipe_when_valid_param_is_sent(
    requests_mock,
    client,
    query_param,
    ingredient_return,
    spoonacular_ingredient_response,
):
    # ARRANGE
    base_url = "https://api.spoonacular.com/recipes"
    endpoint = "findByIngredients"
    requests_mock.get(
        f"{base_url}/{endpoint}", json=spoonacular_ingredient_response
    )

    # ACT
    response = client.get(f"/recipes?i={query_param}")

    # ASSERT
    assert response.json() == ingredient_return
    assert response.status_code == HTTP_200_OK


@pytest.mark.parametrize(
    "query_param, total_error", [("", 0), ("onions,tomatoes,eggs,carrots", 4)]
)
@pytest.mark.django_db
def test_should_return_forbidden_when_params_are_invalid(
    requests_mock,
    client,
    query_param,
    spoonacular_ingredient_response,
    total_error,
):
    # ARRANGE
    base_url = "https://api.spoonacular.com/recipes"
    endpoint = "findByIngredients"
    requests_mock.get(
        f"{base_url}/{endpoint}", json=spoonacular_ingredient_response
    )

    # ACT
    response = client.get(f"/recipes?i={query_param}")

    # ASSERT
    assert response.status_code == HTTP_403_FORBIDDEN
    assert (
        f"Should get 1 to 3 ingredients but got {total_error}"
        in response.json()[0]
    )


# TODO test when spoonacular is problematic
# @pytest.mark.django_db
# def test_should_return_unprocessable_entity_when_spoonacular_api_not_working(
#         requests_mock,
#         client,
# ):
#     # ARRANGE
#     base_url = 'https://api.spoonacular.com/recipes'
#     endpoint = 'findByIngredients'
#     requests_mock.get(f'{base_url}/{endpoint}', status_code=HTTP_408_REQUEST_TIMEOUT)
#
#     # ACT
#     response = client.get(
#             '/recipes?i=onion'
#         )
#
#     # ASSERT
#     print(response.json())
#     # assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY
