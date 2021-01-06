
from django.db import models
from backend.settings import MEDIA_ROOT
from users.models import UserProfile


class Book(models.Model):

    seller = models.ForeignKey(to=UserProfile,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return f'{self.title}'
