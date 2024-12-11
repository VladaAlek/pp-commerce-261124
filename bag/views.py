from django.shortcuts import render, redirect

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified course to the shopping bag """
    quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1 if not provided
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag  # Update the session with the new bag data
    return redirect(redirect_url)