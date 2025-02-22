# Generated by Django 4.2.16 on 2024-12-04 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=255)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(blank=True, null=True, upload_to='RecipeImage/')),
                ('recipe_slug', models.SlugField(unique=True)),
                ('recipe_type', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='App.recipe')),
            ],
        ),
    ]
