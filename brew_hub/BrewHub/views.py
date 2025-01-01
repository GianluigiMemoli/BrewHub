from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def index(request):
    return HttpResponseRedirect("/recipe")
