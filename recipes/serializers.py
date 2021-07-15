from rest_framework import serializers


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class RecipeListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    url = serializers.URLField()
    ingredients = serializers.ListField(IngredientSerializer)
