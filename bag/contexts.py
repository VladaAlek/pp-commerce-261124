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
    purchased_courses = request.session.get('purchased_courses', [])

    for item_id, quantity in bag.items():
        course = get_object_or_404(Category, pk=item_id)
        total += course.price * quantity
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': course,
        })

    if total > settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDART_DISCOUNT_PERCENTAGE / 100)
        discounted_total = total - discount
        grand_total = discounted_total
    else:
        discounted_total = total
        grand_total = total
        discount_delta = settings.DISCOUNT_THRESHOLD - total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'discounted_total': discounted_total,
        'grand_total': grand_total,
        'discount_delta': discount_delta,
        'STANDART_DISCOUNT_PERCENTAGE': settings.STANDART_DISCOUNT_PERCENTAGE,
        'DISCOUNT_THRESHOLD': settings.DISCOUNT_THRESHOLD,
        'purchased_courses': purchased_courses,
    }
    return context