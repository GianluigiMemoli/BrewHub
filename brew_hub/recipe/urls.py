from django.urls import path
from django.urls.conf import include
from recipe.views import (
    RecipeListView,
    CreateRecipeView,
    create_stage,
    stage_ingredients,
)

app_name = "recipe"
urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe_list"),
    path("create/", CreateRecipeView.as_view(), name="recipe_create"),
    path("create/<recipe>/stage", create_stage, name="stage_create"),
    path(
        "create/<recipe>/stage/<stage>/ingredients",
        stage_ingredients,
        name="stage_ingredients",
    ),
]
