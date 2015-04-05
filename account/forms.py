__author__ = 'Zhang_Rui'

from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class loginForm(AuthenticationForm):
    username = forms.CharField(required = True)
    password = forms.CharField(widget=forms.PasswordInput(),required = True)

    class Meta:
        fields = ('username', 'password')


class EditProfileForm(forms.ModelForm):

    phone = forms.IntegerField(required = True)

    class Meta:
        model = UserProfile
        fields = ('display_name',
                  'gender',
                  'photo',
                  'introduction',
                  'address',
                  'postal_code',
                  'country',
                  'phone',
                  'ItemType'
                 )
