from django import forms
from user.models import User, AuthUser

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        field = ('user_id', 'email', )

class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        field = ('auth_user_id', )