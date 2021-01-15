from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import Book
from .forms import BookForm


def home(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'title': 'Audio Books'
    }
    return render(request, 'home.html', context=context)


def displayBook(request, id):
    book = Book.objects.get(pk=id)
    context = {
        'book': book,
    }
    return render(request, 'display_book.html', context=context)


@login_required
def createBook(request):
    if request.method == 'GET':
        form = BookForm()
        context = {'form': form}
        return render(request, 'create_book.html', context=context)

    elif request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller_id = request.user.id
            book.save()
            messages.success(request, "New book has been created!")
            return redirect(reverse('display_listings'))
        else:
            messages.error(request, "New book was not created.")
            return redirect(reverse('create_book'))


@login_required
def deleteBook(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(request, "Book has been deleted!")
    return redirect(reverse('home'))


@login_required
def updateBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == "GET":
        form = BookForm(instance=book)
        context = {
            'form': form,
            'book': book,
        }
        return render(request, 'update_book.html', context=context)

    elif request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book has been update!")
        else:
            messages.success(request, "Book was not update.")
        context = {
            'form': form
        }
        return redirect(reverse('display_book', args=[id]))
