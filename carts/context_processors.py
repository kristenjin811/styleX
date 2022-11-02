from .models import Cart, CartItem
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist
def counter(request):
  cart_count = 0
  if 'admin' in request.path:
    return {}
  else:
    try:
      cart = Cart.objects.filter(cart_id=_cart_id(request))
      cart_items = CartItem.objects.all().filter(cart=cart[:1]) # only 1 for each product\
      for cart_item in cart_items:
        cart_count += cart_item.quantity
    except Cart.ObjectDoesNotExist:
      cart_count = 0
  return dict(cart_count=cart_count)
