from django.contrib import admin
from .models import Order
from django.contrib import messages
from django.utils.translation import ngettext


class OrderAdmin(admin.ModelAdmin):
    list_display = ['creation_datetime', 'buyer', 'product', 'status', 'quantity',
                    'modification_datetime']
    ordering = ['creation_datetime']
    actions = ['make_inDelivery']
    date_hierarchy = 'creation_datetime'

    def make_inDelivery(self, request, queryset):
        updated = queryset.update(status="ID")
        self.message_user(request, ngettext(
            '%d order was successfully marked as IN_DELIVERY.',
            '%d orders were successfully marked as IN_DELIVERY.',
            updated,
        ) % updated, messages.SUCCESS)

    make_inDelivery.short_description = "Mark selected orders as IN_DELIVERY"


admin.site.register(Order, OrderAdmin)
