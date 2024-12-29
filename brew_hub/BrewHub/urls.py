from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("recipe/", include("recipe.urls")),
]
