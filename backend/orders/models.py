from django.db import models
from users.models import UserProfile
from books.models import Book


ORDER_STATUS = [
    ('OC', 'ORDER CREATED'),
    ('PC', 'PAYMENT COMPLETED'),
    ('ID', 'IN DELIVERY'),
    ('OD', 'ORDER DELIVERED')
]


class Order(models.Model):
    buyer = models.ForeignKey(to=UserProfile,
                              on_delete=models.CASCADE)
    product = models.ForeignKey(to=Book,
                                on_delete=models.CASCADE)
    status = models.CharField(max_length=2,
                              choices=ORDER_STATUS,
                              default='OC')
    creation_datetime = models.DateField(auto_now_add=True)
    modification_datetime = models.DateField(auto_now=True)
    quantity = models.IntegerField(default=1)

    @property
    def get_total_cost(self):
        return self.quantity * self.product.price
