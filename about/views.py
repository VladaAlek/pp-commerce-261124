from django.shortcuts import render
from django.conf import settings

def about(request):
    """ A view to return the about page """
    return render(request, 'about/about.html')
