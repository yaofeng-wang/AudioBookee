import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import F
from django.contrib import messages

from books.models import Book
from .models import Order
from users.models import UserProfile


@login_required
def displayOrders(request, id):
    seller = UserProfile.objects.get(pk=id)
    orders = Order.objects.filter(product__seller=seller)
    context = {
        'orders': orders,
        'title': 'Order history',
        'empty_list_text': "No history :(",
    }
    return render(request, 'display_orders.html',
                  context)


@login_required
def displayPurchases(request, id):
    buyer = UserProfile.objects.get(pk=id)
    orders = Order.objects.filter(buyer=buyer).exclude(status='OC')
    context = {
        'orders': orders,
        'title': 'Buying history',
        'empty_list_text': "No history :(",
    }
    return render(request, 'display_purchases.html',
                  context)


@login_required
def cart(request):
    orders = Order.objects.filter(buyer=request.user).filter(status='OC')
    context = {
        'orders': orders,
        'empty_list_text': "Cart is empty :(",
    }
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    orders = Order.objects.filter(buyer=request.user, status='OC')

    total = 0
    for order in orders:
        total += order.get_total_cost
    context = {'orders': orders, 'total': total}

    return render(request, 'checkout.html', context)


@login_required
def updateOrder(request):

    if request.method == "POST":
        data = json.loads(request.body)
        product_id, action = data['product_id'], data['action']

        book = Book.objects.get(pk=product_id)
        orders = Order.objects.filter(
            buyer=request.user, product=book, status='OC')

        if action == 'add':
            if orders.exists():
                orders.update(quantity=F('quantity')+1)
            else:
                Order.objects.create(buyer=request.user, product=book)
            messages.success(request, "An item has been added to cart!")
            return JsonResponse({'action': action,
                                 'product': orders.first().product_id,
                                 'quantity': orders.first().quantity})
        elif action == 'remove':
            if orders.exists():
                order = orders.first()
                order.delete()
                messages.success(
                    request, "An item has been deleted from cart!")
                return JsonResponse({'action': action,
                                     'product': order.product_id,
                                     'quantity': order.quantity})
            else:
                messages.success(request, "Item was not deleted from cart!")

    else:
        return redirect(reverse('home'))


@login_required
def makePayment(request):
    if request.method == "POST":
        orders = Order.objects.filter(buyer=request.user, status='OC')
        orders.update(status='PC')
        messages.success(request, "Payment was successful!")
    return redirect(to='home')
