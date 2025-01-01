from django.forms import (
    ModelForm,
    CharField,
    TextInput,
    IntegerField,
    NumberInput,
    ChoiceField,
    Select,
)

from django.utils.translation import gettext as _
from recipe.models import Recipe, Stage, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description"]


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ["title", "notes", "days_duration"]

    field_order = ["title", "days_duration", "notes"]


class IngredientForm(ModelForm):
    title = CharField(
        widget=TextInput(
            attrs={
                "class": "is-inline",
                "placeholder": _("Ingredient"),
            }
        )
    )
    quantity = IntegerField(
        widget=NumberInput(attrs={"class": "is-inline", "placeholder": _("Quantity")})
    )

    measure_unit = ChoiceField(
        widget=Select(attrs={"class": "is-inline"}),
        choices=Ingredient.MeasureUnit.choices,
    )

    def __init__(self, hide_labels=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hide_labels:
            for field in self.fields:
                self.fields[field].label = ""

    class Meta:
        model = Ingredient
        fields = ["title", "quantity", "measure_unit"]

    field_order = ["title", "quantity", "measure_unit"]
