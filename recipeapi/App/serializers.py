from rest_framework import serializers
from App.models import Recipe, Ingredients


# ============== First Way Start ==================
# class IngredientsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredients
#         # fields = "__all__"
#         fields = ["ingredient_name"]

# class RecipeSerializer(serializers.ModelSerializer):
#     ingredients = IngredientsSerializer(many=True)
#     class Meta:
#         model = Recipe
#         fields = ["recipe_name", "recipe_description", "recipe_image", "recipe_slug", "recipe_type", "ingredients"]

# ============== First Way End ==================


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        # fields = "__all__"  
        fields = ["ingredient_name"]

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

    def to_representation(self, instance):
        print("Instance: ", instance)
        data = super().to_representation(instance)
        data["ingredients"] = IngredientsSerializer(instance.ingredients.all(), many=True).data
        print("Data: ", data)
        return data
    

class CreateRecipeSerializer(serializers.ModelSerializer):
    recipe_slug = serializers.SlugField(allow_null=True, required=False)

    # Allowing Only Non-Empty Ingredients:
    # Added allow_empty=False to ensure the ingredients list isn't empty.
    ingredients = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    class Meta:
        model = Recipe
        fields = "__all__"

    def create(self, validated_data):
        print("Validated Data: ", validated_data)
        ingredients = validated_data.pop("ingredients")
        print("Ingredients: ", ingredients)

        recipe = Recipe.objects.create(**validated_data)
        print("Recipe: ", recipe)
        for ingredient in ingredients:
            Ingredients.objects.create(recipe=recipe, ingredient_name=ingredient)

        return recipe