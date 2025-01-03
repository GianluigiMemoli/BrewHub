from http.client import HTTPResponse

from django.http import HttpResponseRedirect
from django.urls import path
from django.urls.conf import include

from BrewHub.views import index

urlpatterns = [
    path("", index),
    path("accounts/", include("allauth.urls")),
    path("recipe/", include("recipe.urls")),
]
