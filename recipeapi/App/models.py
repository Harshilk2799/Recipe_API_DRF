from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="RecipeImage/", null=True, blank=True)
    recipe_slug = models.SlugField(unique=True)
    recipe_type = models.CharField(max_length=255, choices=(("Veg", "Veg"), ("Non-Veg", "Non-Veg")))

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient_name = models.CharField(max_length=255)