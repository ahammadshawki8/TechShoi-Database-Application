# Importing necessary modules & libraries
from django import forms


# A simple LoginForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)