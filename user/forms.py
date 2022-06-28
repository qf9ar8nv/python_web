from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm

from user.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user
