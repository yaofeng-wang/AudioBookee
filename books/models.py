from PIL import Image
from django.db import models
from backend.settings import MEDIA_ROOT
from users.models import UserProfile
from django.urls import reverse
from django.conf import settings
from django_resized import ResizedImageField


class Book(models.Model):

    seller = models.ForeignKey(to=UserProfile,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    thumbnail = ResizedImageField(
        size=[300, 400], upload_to='books', quality=75, force_format='JPEG')
    image = ResizedImageField(
        size=[500, 300], upload_to='books', quality=75, force_format='JPEG')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('display_book', args=[self.id])
