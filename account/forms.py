from django import forms
from .models import Member
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('photo',)



