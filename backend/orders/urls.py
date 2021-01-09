from django.contrib import admin
from django.urls import include, path
from .views import displayOrders, displayPurchases, cart

urlpatterns = [
    path('to/<int:id>/', displayOrders,
         name="display_orders"),
    path('by/<int:id>/', displayPurchases,
         name="display_purchases"),
    path('cart/', cart, name="cart"),
]
