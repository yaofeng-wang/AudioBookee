from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'home.html', context=context)


def displayBook(request, id):
    book = Book.objects.get(pk=id)
    context = {'book': book}
    return render(request, 'display_book.html', context=context)
