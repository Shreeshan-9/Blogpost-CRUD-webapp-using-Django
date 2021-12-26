from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # we want the form to interact with the model User

        fields = ['username', 'email', 'password1', 'password2']
        
        #the class Meta gives a nested namespace for configurations & keeps the configurations in one place
        # within the configuration, the model that will be affected is User
        # the list which is assigned to the fields are what we want in the form in exact order

    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']