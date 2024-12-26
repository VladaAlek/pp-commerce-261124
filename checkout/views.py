from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    '''
    # You might not need this code above as you set 
    # the values as integers in your model:
    # price = models.IntegerField(null=True, blank=True)
    ''' 
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QIWOXCyC9p9iSxKn9u15QzYcVW0thACoXxu8TyGTJknH3TH8bMtXepsZbqdnJ80yendIzZ2q33eHa0um0E1hkAK00j5hUVsI4',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)