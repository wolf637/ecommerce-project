from django.shortcuts import render, redirect

from .models import Cart
from products.models import Product


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", context={"cart": cart_obj})

def cart_update(request):

    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            prod_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user that product does not exist")
            return redirect("cart:home")
        prod_obj = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if prod_obj in cart_obj.products.all():
            cart_obj.products.remove(prod_obj)
        else:
            cart_obj.products.add(prod_obj)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")