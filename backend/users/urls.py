from django.contrib import admin
from django.urls import path
from .views import userCreation, displayUser, userLogin, userLogout

urlpatterns = [
    path('', userCreation, name="create_user"),
    path('<int:id>/', displayUser, name="display_user"),
    path('login/', userLogin, name="login_user"),
    path('logout/', userLogout, name="logout_user"),

]
