from django.contrib import admin
from django.urls import path
from .views import userCreation, displayUser, userLogin, userLogout, userListings


urlpatterns = [
    path('<int:id>', displayUser, name="display_user"),
    path('register/', userCreation, name="create_user"),
    path('login/', userLogin, name="login_user"),
    path('logout/', userLogout, name="logout_user"),
    path('listings/', userListings, name="display_listings"),
]
