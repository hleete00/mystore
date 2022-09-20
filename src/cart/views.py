from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from store.models import Product


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_qty = int(request.POST.get('productQty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        cart_qty = cart.__len__()
        response = JsonResponse({'qty': cart_qty})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        print(product_id)
        cart.delete(product_id=product_id)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productId'))
        product_qty = int(request.POST.get('productQty'))
        cart.update(product_id=product_id, qty=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total})
        return response
