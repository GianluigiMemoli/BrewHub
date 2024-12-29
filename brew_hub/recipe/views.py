from django.urls.base import reverse_lazy

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from recipe.forms import RecipeForm, StageForm
from recipe.models import Recipe, Stage


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 10


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = "recipe/create_recipe/create_recipe.html"
    form_class = RecipeForm
    success_url = reverse_lazy("recipe:recipe_list")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        self.success_url = reverse_lazy("recipe:stage_create", args=[instance.pk])
        return super().form_valid(form)


def create_stage(request, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    if request.method == "POST":
        pass
    else:
        form = StageForm()
    return render(
        request,
        "recipe/create_recipe/create_stage.html",
        {
            "form": form,
            "recipe": recipe,
        },
    )
