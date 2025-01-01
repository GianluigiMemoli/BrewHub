from http.client import HTTPResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from recipe.forms import RecipeForm, StageForm, IngredientForm
from recipe.models import Recipe, Stage


# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 10


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe/create_recipe/create_recipe.html"
    form_class = RecipeForm
    success_url = reverse_lazy("recipe:recipe_list")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        self.success_url = reverse_lazy("recipe:stage_create", args=[instance.pk])
        return super().form_valid(form)


@login_required
def create_stage(request, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    form = StageForm()
    if request.method == "POST":
        form = StageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            order = recipe.stage_set.count()
            if order > 0:
                order += 1
            instance.order = order
            instance.recipe = recipe
            instance.created_by = request.user
            instance.save()
            return HttpResponseRedirect(
                reverse_lazy("recipe:stage_ingredients", args=[recipe.pk, instance.pk])
            )
    return render(
        request,
        "recipe/create_recipe/create_stage.html",
        {
            "form": form,
            "recipe": recipe,
        },
    )


def stage_ingredients(request, recipe, stage):
    recipe = get_object_or_404(Recipe, pk=recipe)
    stage = get_object_or_404(Stage, pk=stage)
    form = IngredientForm(hide_labels=True)
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            stage.ingredients.add(instance)
    return render(
        request,
        "recipe/create_recipe/stage_ingredients.html",
        {
            "form": form,
            "recipe": recipe,
            "stage": stage,
        },
    )
