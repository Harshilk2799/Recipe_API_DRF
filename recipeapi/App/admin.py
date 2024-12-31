from django.contrib import admin
from App.models import Recipe, Ingredients

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id","recipe_name", "recipe_description", "recipe_image", "recipe_slug", "recipe_type"]


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ["id","recipe", "ingredient_name"]