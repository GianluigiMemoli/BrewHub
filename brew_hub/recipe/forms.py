from django.forms import ModelForm
from recipe.models import Recipe, Stage


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description"]


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ["title", "notes", "days_duration"]

    field_order = ["title", "days_duration", "notes"]
