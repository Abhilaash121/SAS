from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Create
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#Update
class UserUpdateForm(forms.ModelForm):  # changes in the User model
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):  # changes in the Profile model 
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']