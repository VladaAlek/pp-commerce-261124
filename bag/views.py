from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
from django.contrib import messages
from products.models import Category


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified course to the shopping bag """

    category = get_object_or_404(Category, pk= item_id)
    quantity = int(request.POST.get('quantity', 1)) 
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {category.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    category = get_object_or_404(Category, pk= item_id)
    try:
        bag = request.session.get('bag', {})
        if item_id in bag:
            bag.pop(item_id)
            request.session['bag'] = bag
            messages.warning(request, f'You removed {category.name} course from your bag')
            
           
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing category {e} from your bag')
        print(e)
        return HttpResponse(status=500)
