from rest_framework import routers

from recipes.views import RecipeList

recipes_router = routers.DefaultRouter(trailing_slash=False)
recipes_router.register(
    prefix=r"recipes", viewset=RecipeList, basename="recipes"
)

urlpatterns = recipes_router.urls
