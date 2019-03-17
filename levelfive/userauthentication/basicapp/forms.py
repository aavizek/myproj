from django import forms
from .models import UserPortfolio
from django.contrib.auth.models import  User
from .models import UserPortfolio
class UserPortfolioForm(forms.ModelForm):
    class Meta():
        model=UserPortfolio
        fields=('portfolio','picture')
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
