from django import forms
from .models import UserImageModel

class UserImageForm(forms.ModelForm):
    class Meta():
        model = UserImageModel
        fields = ['image']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
        
    username = forms.CharField(max_length=200)
    email = forms.EmailField(required=True)
    mobile_no = forms.IntegerField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username','email','mobile_no', 'password1', 'password2')

  
        


