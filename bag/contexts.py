from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Category

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    discount_delta = 0
    bag = request.session.get('bag', {})


    for item_id, quantity in bag.items():
        course = get_object_or_404(Category, pk=item_id)
        total += course.price
        product_count += 1
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': course,
    })

    
    if total > settings.DISCOUNT_TRESHOLD:
        discount = total * Decimal(settings.STANDART_DISCOUNT_PERCENTAGE / 100)
        discounted_total = total - discount
        discount_delta = total - discount_delta
    else:
        discounted_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'STANDART_DISCOUNT_PERCENTAGE': settings.STANDART_DISCOUNT_PERCENTAGE,
        'DISCOUNT_TRESHOLD': settings.DISCOUNT_TRESHOLD,
    }
    return context