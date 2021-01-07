from django.shortcuts import render, redirect
from .forms import UserProfileForm, LoginForm, UpdateProfileForm
from django.urls import reverse
from .models import UserProfile
from django.db.models import Model
from django.contrib.auth import authenticate, login, logout
from books.models import Book
from django.contrib.auth.decorators import login_required


def userCreation(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            UserProfile.objects.create_user(username=username,
                                            password=password)
            return redirect(to=reverse('create_user'))
    elif request.method == 'GET':
        form = UserProfileForm()
    return render(request,
                  'create_user.html',
                  context={'form': form})


@login_required
def displayUser(request, id):
    try:
        if request.method == 'GET':
            user = UserProfile.objects.get(id=id)
            form = UpdateProfileForm(initial={'username': user.username})
        elif request.method == 'POST':
            user = UserProfile.objects.get(id=id)
            form = UpdateProfileForm(request.POST)
            if not form.is_valid():
                return redirect(to=reverse('display_user', id=id))
            username = form.cleaned_data['username'] if form.cleaned_data['username'] else user.username

            user.username = username
            user.save()
        books = Book.objects.filter(seller=id)
    except:
        return redirect(to=reverse('home'))
    context = {'form': form, 'books': books}
    return render(request, 'display_user.html', context)


def userLogin(request):
    print(request.method)
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html',
                      {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect(to=reverse('home'))

    return redirect(to=reverse('login_user'))


def userLogout(request):
    logout(request)
    return redirect(to=reverse('home'))
