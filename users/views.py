from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from books.models import Book
from .models import UserProfile
from .forms import UserProfileForm, LoginForm, UpdateProfileForm


def userCreation(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            UserProfile.objects.create_user(username=username,
                                            password=password)
            messages.success(request, "New user was created!")
            return redirect(to=reverse('login_user'))
        else:
            messages.error(request, "New user was not created.")
            return redirect(to=reverse('create_user'))

    # GET method
    form = UserProfileForm()
    return render(request,
                  'create_user.html',
                  context={'form': form})


@login_required
def displayUser(request, id):
    user = UserProfile.objects.get(id=id)

    if request.method == 'GET':
        form = UserProfileForm(initial={'username': user.username})

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'display_user.html', context)


def userLogin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html',
                      {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,
                                password=password)
            if user is None:
                messages.error(request, 'Invalid login credentials.')
                return redirect(to=reverse('login_user'))
            else:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect(to=reverse('home'))
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect(to=reverse('login_user'))


@login_required
def userLogout(request):
    logout(request)
    messages.success(request, f'Good-bye!')
    return redirect(to=reverse('home'))


@login_required
def userListings(request):
    books = Book.objects.filter(seller=request.user)
    context = {
        'books': books,
    }
    return render(request, 'display_listings.html', context)
