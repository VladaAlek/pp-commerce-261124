from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Category
from profiles.models import PurchasedCourse


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified course to the shopping bag """

    category = get_object_or_404(Category, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    message_shown = request.session.get('message_shown', {})

    # getting purchased courses from the database
    if request.user.is_authenticated:
        purchased_courses = PurchasedCourse.objects.filter(user=request.user).values_list('course_id', flat=True)
    else:
        purchased_courses = []

    # preventing adding the course if already exists in the database

    if item_id in purchased_courses:
        message.warning(request, f'You have alredy purchased {category.name}')
        return redirect(redirect_url)


    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        if str(item_id) in message_shown:
            messages.warning(request, f'You cannot add {category.name} course in your bag twice.')
        else:
            messages.success(request, f'Added {category.name} course to your bag.')
            message_shown[str(item_id)] = True  # Mark message as shown for this item

    request.session['bag'] = bag
    request.session['message_shown'] = message_shown
    return redirect(redirect_url)



def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    category = get_object_or_404(Category, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        message_shown = request.session.get('message_shown', {})

        if item_id in bag:
            bag.pop(item_id)
            request.session['bag'] = bag
            if str(item_id) in message_shown: # search for the specific course id
                message_shown.pop(str(item_id))  # Reset message for this item
                request.session['message_shown'] = message_shown # reset variable message_shown

            messages.info(request, f'You removed {category.name} course from your bag')
           
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing category {e} from your bag')
        print(e)
        return HttpResponse(status=500)

