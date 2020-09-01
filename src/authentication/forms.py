from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="",max_length=10,widget=forms.TextInput(attrs={"placeholder": "Enter username", "class": "fadeIn second", "id": "login"}))
    password = forms.CharField(label="",max_length=10,widget=forms.TextInput(attrs={"placeholder": "Enter password","class": "fadeIn third", "id": "password"}))