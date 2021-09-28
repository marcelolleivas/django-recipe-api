from drf_yasg.openapi import (
    IN_QUERY,
    TYPE_ARRAY,
    TYPE_STRING,
    Items,
    Parameter,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from .serializers import RecipeListSerializer
from .services import SpoonacularApiService, SpoonacularApiServiceError


class RecipeList(mixins.ListModelMixin, viewsets.GenericViewSet):
    spoon_service = SpoonacularApiService()
    serializer_class = RecipeListSerializer
    params = Parameter(
        name="i",
        in_=IN_QUERY,
        type=TYPE_ARRAY,
        items=Items(type=TYPE_STRING),
        required=True,
    )

    @swagger_auto_schema(manual_parameters=[params])
    def list(self, request, *args, **kwargs):
        try:
            ingredients = request.GET.get("i")
            data = self.spoon_service.get_by_ingredients(ingredients)
            return Response(data)
        except SpoonacularApiServiceError as error:
            return Response(error.args[0], status=HTTP_403_FORBIDDEN)

    def get_queryset(self):
        return
