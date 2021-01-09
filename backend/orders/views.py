from django.shortcuts import render
from .models import Order
from users.models import UserProfile
from books.models import Book
from django.contrib.auth.decorators import login_required


@login_required
def displayOrders(request, id):
    seller = UserProfile.objects.get(pk=id)
    orders = Order.objects.filter(product__seller=seller)
    context = {
        'orders': orders
    }
    return render(request, 'display_orders.html',
                  context)


@login_required
def displayPurchases(request, id):
    buyer = UserProfile.objects.get(pk=id)
    orders = Order.objects.filter(buyer=buyer).exclude(status='OC')
    context = {
        'orders': orders
    }
    return render(request, 'display_purchases.html',
                  context)


@login_required
def cart(request):
    orders = Order.objects.filter(buyer=request.user).filter(status='OC')
    context = {
        'orders': orders
    }
    return render(request, 'cart.html', context)


def checkout(request):
    pass


def updateOrder(request):
    pass
