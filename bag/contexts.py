from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    discount = 0

    if total > settings.DISCOUNT_TRESHOLD:
        discount = total * Decimal(settings.STANDART_DISCOUNT_PERCENTAGE / 100)
        discounted_total = total - discount
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