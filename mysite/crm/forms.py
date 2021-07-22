from django import forms

class User_login(forms.Form):
    email=forms.CharField()
    password=forms.CharField()