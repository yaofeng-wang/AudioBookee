from django.contrib import admin
from django.urls import include, path
from .views import displayOrders, displayPurchases, cart, updateOrder, checkout, makePayment

urlpatterns = [
    path('to/<int:id>/', displayOrders,
         name="display_orders"),
    path('by/<int:id>/', displayPurchases,
         name="display_purchases"),
    path('cart/', cart, name="cart"),
    path('update-order', updateOrder, name="update_order"),
    path('checkout', checkout, name="checkout"),
    path('make-payment', makePayment, name="make_payment"),
]
