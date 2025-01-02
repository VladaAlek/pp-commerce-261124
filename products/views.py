from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Material
from .forms import CategoryForm, MaterialForm
from django.contrib import messages



def all_categories(request):
    """ A view to show all categories """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)


def individual_category(request, category_id):
    """ A view to show individual category """

    # Get the category
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'category': category,
    }

    return render(request, 'products/individual_category.html', context)

    

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



def add_product(request):
    """ Add a product and its materials to the store """
    category_form = CategoryForm()
    material_form = MaterialForm()

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        material_form = MaterialForm(request.POST, request.FILES)
        if category_form.is_valid() and material_form.is_valid():
            category = category_form.save()
            material = material_form.save(commit=False)
            material.category = category
            material.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        category_form = CategoryForm()
        material_form = MaterialForm()

            
    template = 'products/add_product.html'
    context = {
        'category_form': category_form,
        'material_form': material_form,
    }

    return render(request, template, context)


