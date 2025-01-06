from django.shortcuts import render
from django.conf import settings

def about(request):
    """ A view to return the about page """
    print(settings.TEMPLATES[0]['DIRS'])  # Debug template directories
    return render(request, 'about/about.html')
