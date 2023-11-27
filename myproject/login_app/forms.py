from django import forms
from django.forms import PasswordInput


class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=24, widget=PasswordInput)


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=30, label="Логин")
    password_1 = forms.CharField(max_length=24, widget=PasswordInput, label="Пароль")
    password_2 = forms.CharField(max_length=24, widget=PasswordInput, label="Повторный пароль")
