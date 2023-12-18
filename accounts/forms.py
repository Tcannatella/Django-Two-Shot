from django import forms
from receipts.models import Account
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )

