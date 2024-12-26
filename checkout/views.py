from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QIWOXCyC9p9iSxKn9u15QzYcVW0thACoXxu8TyGTJknH3TH8bMtXepsZbqdnJ80yendIzZ2q33eHa0um0E1hkAK00j5hUVsI4',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)