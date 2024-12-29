from base.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
User = get_user_model()


class Recipe(BaseModel):
    class RecipeStatus(models.TextChoices):
        DRAFT = "DRAFT", _("Draft")
        PUBLISHED = "PUBLISHED", _("Published")
        ARCHIVED = "ARCHIVED", _("Archived")

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=RecipeStatus.choices, default=RecipeStatus.DRAFT)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Ingredient(BaseModel):
    class MeasureUnit(models.TextChoices):
        g = "g", _("gram")
        kg = "kg", _("kilogram")
        ml = "ml", _("milliliter")
        l = "l", _("liter")

    title = models.CharField(max_length=255)
    measure_unit = models.CharField(
        choices=MeasureUnit.choices,
        null=False,
        blank=False,
        verbose_name=_("Unit of measure"),
    )
    quantity = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Stage(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField()
    ingredients = models.ManyToManyField("Ingredient", related_name="stages")
    days_duration = models.PositiveIntegerField(
        null=False, blank=False, verbose_name=_("Duration in days")
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Brew(BaseModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    current_stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
