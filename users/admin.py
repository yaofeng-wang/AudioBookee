from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'last_login', 'date_joined']

    # attributes from the User class that UserProfile class ignores
    exclude = ['first_name', 'last_name', 'email']


admin.site.register(UserProfile, UserProfileAdmin)
