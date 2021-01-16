from PIL import Image
from django.db import models
from backend.settings import MEDIA_ROOT
from users.models import UserProfile
from django.urls import reverse
from django.conf import settings
from django_resized import ResizedImageField
from django.conf import settings
from django.utils.html import format_html


class Book(models.Model):

    seller = models.ForeignKey(to=UserProfile,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    # original image
    image = models.ImageField(upload_to='books')
    # resize image only if it is larger than 300 x 400
    # a smaller version of original image
    thumbnail = ResizedImageField(
        size=[300, 400], upload_to='books', quality=75, force_format='JPEG')
    audio = models.FileField(upload_to='audio')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('display_book', args=[self.id])

    def audio_player(self):
        if self.audio:
            file_url = settings.MEDIA_URL + str(self.audio)
            player_string = format_html(
                f'<audio src="{file_url}" controls>Your browser does not support the audio element.</audio>')
            return player_string
    audio_player.allow_tags = True
    audio_player.short_description = ('Audio file player')
