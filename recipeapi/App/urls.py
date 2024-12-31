from django.urls import path
from App import views

urlpatterns = [
    path('recipe/', views.RecipeAPI.as_view()),
]
