from django import template
from order.models import Cart, Product, Order
register = template.Library()

@register.filter
def cart_view(user):
    cart = Cart.objects.filter(user = user,purchased = False)
    if cart.exists():
        return cart
    else:
        return ValueError('No cart found')
    

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user,purchased=False)
    if order.exists():
        return order[0].get_totals
    else:
        return 0