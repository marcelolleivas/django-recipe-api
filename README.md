Recipe API
----------
Is a recipe API that generates data from Spoonacular API based on ingredients 
you ask for, limited to 3 ingredients.

Installation
============
Use the package manager [poetry](https://github.com/python-poetry/poetry) to install it's dependencies.

```bash
poetry shell

poetry install
```

Usage
=====
Make sure you created ```.env``` file with ```API_KEY``` configured.

You can generate your own key by creating an account on [Spoonacular website](https://spoonacular.com/food-api/console#Dashboard).

For now you just can use the API locally

```bash
python manage.py runserver
```

Then you can make requests to ```http://127.0.0.1:8000/recipes``` using
```ingredients``` as query params.

Or just do it calling the service with python

```python
from recipes.services import SpoonacularApiService

SpoonacularApiService().get_by_ingredients('<insert ingredients here>')
```