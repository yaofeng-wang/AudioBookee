from django.contrib import admin
from django.urls import path
from .views import home, displayBook, createBook, deleteBook, updateBook
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('<int:id>/', displayBook, name="display_book"),
    path('update/<int:id>/', updateBook, name="update_book"),
    path('delete/<int:id>/', deleteBook, name="delete_book"),
    path('create/', createBook, name="create_book"),
]
