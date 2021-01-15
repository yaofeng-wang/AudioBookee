from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password'}),
        }


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    fields = ['username', 'password']


class UpdateProfileForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
