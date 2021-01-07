from django.contrib import admin
from django.urls import path
from .views import home, displayBook
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('<int:id>/', displayBook, name="display_book")
]
