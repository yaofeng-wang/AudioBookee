from django.contrib import admin
from .models import Book
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):
    list_display = ['admin_thumbnail', 'title',
                    'price', 'seller', 'audio_player']

    def admin_thumbnail(self, obj):
        return format_html('<img src="{}" style="height:150px; width:150px;" />'.format(obj.thumbnail.url))
    admin_thumbnail.short_description = 'Admin page thumbnail'


admin.site.register(Book, BookAdmin)
