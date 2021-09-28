![GitHub Workflow Status](https://img.shields.io/github/workflow/status/marcelolleivas/django-recipe-api/pipeline)

Recipe API
==========
Is a simple project that makes Spoonacular API requests to get recipes.

Requirements
------------
- At least Python 3.8.XX;
- [Poetry](https://github.com/python-poetry/poetry) installed;
- Token generated on [Spoonacular website](https://spoonacular.com/food-api/console#Dashboard);

Installation
------------
Having poetry installed, you can run the commands:

```bash
poetry shell

poetry install
```

Usage
-----
Make sure you created ```.env``` file with ```API_KEY``` configured. You can generated your own key accessing [Spoonacular website](https://spoonacular.com/food-api/console#Dashboard). With your ```.env```  file configured, you just need to follow the guidelines below.
```bash
python manage.py runserver
```
This will run the application locally. Now you can make requests using ```http://127.0.0.1:8000/recipes``` using ```i```
as query param.

Example:
--------
```[GET]  http://127.0.0.1:8000/recipes?i=onions,tomatoes,eggs```
##### Response
```json
[
  {
    "title": "Scramble Eggs with Tomato and Scallions (Huevos Revueltos con Tomate y Cebolla)",
    "image": "https://spoonacular.com/recipeImages/226705-312x231.jpg",
    "ingredients": [
      "eggs",
      "scallions",
      "tomatoes"
    ]
  }
]
```

Documentation
------------
For more details about the API, you can have access to ```swagger``` by running
```bash
python manage.py runserver
```
And accessing ```http://127.0.0.1:8000/docs```.