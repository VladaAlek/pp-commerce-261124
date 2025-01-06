from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Material
from .forms import CategoryForm, MaterialForm
from django.contrib import messages
from django.forms import modelformset_factory
import random
MaterialFormSet = modelformset_factory(Material, fields='__all__')


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


def add_course(request):
    """ Add a category/course to the store """
    category_form = CategoryForm()
    category_id = None  
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save()
            category_id = new_category.id  # Get category_id after saving
            messages.success(request, 'Successfully added online course!')
            return redirect(reverse('add_material', args=[category_id]))  # Redirect with category_id
        else:
            messages.error(request, 'Failed to add online course. Please ensure the form is valid.')
    else:
        form = CategoryForm()

        
    template = 'products/add_product.html'
    context = {
        'category_form': category_form,
        'category_id': category_id,
    }

    return render(request, template, context)


def add_material(request, category_id):
    """ Add a material to the online course """
    category = get_object_or_404(Category, pk=category_id) 
    material_form = MaterialForm() 
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.category = category
            material.save()
            messages.success(request, 'Successfully added online material!')
            return redirect(reverse('categories'))
        else:
            messages.error(request, 'Failed to add material to the course. Please ensure the form is valid.')
    else:
        form = MaterialForm()
        
    template = 'products/add_material.html'
    context = {
        'material_form': material_form,
        'category_id': category_id,
    }

    return render(request, template, context)


def edit_course(request, category_id):
    """ Edit a course and its materials in the store """
    category = get_object_or_404(Category, pk=category_id)
    materials = Material.objects.filter(category=category)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES, instance=category)
        material_formset = MaterialFormSet(request.POST, request.FILES, queryset=materials)
        if category_form.is_valid() and material_formset.is_valid():
            category_form.save()
            material_formset.save()
            messages.success(request, 'Successfully updated course and materials!')
            return redirect(reverse('edit_course', args=[category.id]))
        else:
            messages.error(request, 'Failed to update. Please ensure the forms are valid.')
    else:
        category_form = CategoryForm(instance=category)
        material_formset = MaterialFormSet(queryset=materials)

    template = 'products/edit_product.html'
    context = {
        'category_form': category_form,
        'material_formset': material_formset,
        'category': category,
    }

    return render(request, template, context)


def delete_course(request, category_id):
    """ Delete a course from the store """
    course = get_object_or_404(Category, pk=category_id)
    course.delete()
    messages.success(request, 'Course {{ category.name }}deleted!')
    return redirect(reverse('categories'))