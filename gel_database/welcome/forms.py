from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput())
      
class UserLogin(forms.Form):
    username = forms.CharField(label="Username", max_length=30, help_text=False)
    password = forms.CharField(label="Password", max_length=30, help_text=False, widget=forms.PasswordInput())
