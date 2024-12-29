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
        self.success_url = reverse_lazy(
            "recipe:stage_create", kwargs={"recipe": instance.pk}
        )
        return super().form_valid(form)


class CreateStageView(CreateView):
    model = Stage
    template_name = "recipe/create_stage/create_stage.html"
    form_class = StageForm
    recipe = None

    def get(self, request, *args, **kwargs):
        self.recipe = get_object_or_404(Recipe, pk=request.get("recipe"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = self.recipe
        return context
