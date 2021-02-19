from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ("first_name", "email", "password")
