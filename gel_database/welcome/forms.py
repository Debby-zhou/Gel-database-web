from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label="Username", max_length=30, help_text=False)
    email = forms.EmailField(label="Email", help_text=False)
    password = forms.CharField(label="Password", max_length=30, help_text=False, widget=forms.PasswordInput())

class UserLogin(forms.Form):
    username = forms.CharField(label="Username", max_length=30, help_text=False)
    password = forms.CharField(label="Password", max_length=30, help_text=False, widget=forms.PasswordInput())
