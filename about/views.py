from django.shortcuts import render
from . import views


def about(request):
    """ A view to return the index page """

    return render(request, 'about/about.html')