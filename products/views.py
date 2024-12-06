from django.shortcuts import render, get_object_or_404
from .models import Category, Material


def all_categories(request):
    """ A view to show all categories """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)


def category_detail(request, category_id):
    """ A view to show the materials in a specific category """
    
    # Get the category
    category = get_object_or_404(Category, pk=category_id)

    # Get all materials under the category
    materials = Material.objects.filter(category=category)

    context = {
        'category': category,
        'materials': materials,
    }

    return render(request, 'products/material.html', context)

