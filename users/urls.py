from django.contrib import admin
from django.urls import path
from .views import createUser, updateUser, userLogin, userLogout, userListings


urlpatterns = [
    path('<int:id>', updateUser, name="update_user"),
    path('register/', createUser, name="create_user"),
    path('login/', userLogin, name="login_user"),
    path('logout/', userLogout, name="logout_user"),
    path('listings/', userListings, name="display_listings"),
]
