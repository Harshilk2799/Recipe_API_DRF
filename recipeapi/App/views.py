from rest_framework.views import APIView
from App.serializers import RecipeSerializer, CreateRecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from App.models import Recipe


class RecipeAPI(APIView):
    def get(self, request):
        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = CreateRecipeSerializer(data=request.data)
        if serializer.is_valid():
            recipe = serializer.save()
            
            ingredients = recipe.ingredients.all()
            print("Ingredients:", ingredients)
            
            response = {
                "recipe_name": recipe.recipe_name,
                "recipe_description": recipe.recipe_description,
                "recipe_image": recipe.recipe_image.url if recipe.recipe_image else None,
                "recipe_slug": recipe.recipe_slug,
                "recipe_type": recipe.recipe_type,
                "ingredients": [ingredient.ingredient_name for ingredient in ingredients]
            }
            print("Response: ", response)
            return Response({"data": response}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        recipe_data = request.data.get("id")
        Recipe.objects.get(id=recipe_data).delete()
        return Response({"data": "Recipe Deleted!!!"}, status=status.HTTP_204_NO_CONTENT)