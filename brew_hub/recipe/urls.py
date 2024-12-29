from django.urls import path
from django.urls.conf import include
from recipe.views import RecipeListView, CreateRecipeView, CreateStageView

app_name = "recipe"
urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe_list"),
    path("create/", CreateRecipeView.as_view(), name="recipe_create"),
    path("create/<recipe>/stage", CreateStageView.as_view(), name="stage_create"),
]
