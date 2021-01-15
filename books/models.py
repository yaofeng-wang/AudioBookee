from PIL import Image
from django.db import models
from backend.settings import MEDIA_ROOT
from users.models import UserProfile
from django.urls import reverse
from django.conf import settings


class Book(models.Model):

    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = 500

    seller = models.ForeignKey(to=UserProfile,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('display_book', args=[self.id])

    def save(self, *args, **kwargs):
        # save instance to create image in static folder
        super().save(*args, **kwargs)

        # standardise size of image
    #     self._resize_image()

    # def _resize_image(self):
    #     with Image.open(self.image.path) as image:
    #         image = image.resize((self.IMAGE_WIDTH, self.IMAGE_HEIGHT))
    #         image.save(self.image.path)
