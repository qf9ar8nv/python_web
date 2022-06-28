from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import logout, login
import requests

from user.forms import UserForm, CustomSignupForm
from user.models import User

@login_required(login_url='/user/login')
def update(request):
    if request.method == 'GET':
        context = {'user_name': request.user.username}
        return render(request, 'user/update.html', context)
    else:
        user = request.user
        user_name = request.POST['user_name']
        user.username = user_name
        user.save()

    return redirect('/accounts/profile')

def mainPage(request):
    return redirect('/board/list')

def user_logout(request):
    logout(request)
    return redirect('/user/login')

def user_login(request):
    if request.method == 'POST':
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            login(request, loginForm.get_user())

            return redirect('/board/list')
        else:
            return redirect('/user/login')
    else:
        loginForm = AuthenticationForm()
    return render(request, 'user/login.html', {'loginForm': loginForm})

# Create your views here.
def signup(request):
    if request.method == 'POST':
        signupForm = CustomSignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save(request)
            return redirect('/user/login')
    else:
        signupForm = CustomSignupForm()
    return render(request, 'user/signup.html', {'signupForm': signupForm})

@login_required(login_url='/user/login')
def withdrawal(request):
    user = request.user
    user.delete()
    return redirect('/board/list')

def getCode(request):
    code = request.GET.get('code')

    data = {
        'grant_type': 'authorization_code',
        'client_id': '8fbdff3b1fca2b0721bf238ff092d4b8',
        'redirect_uri': 'http://127.0.0.1:8000/oauth/redirect/',
        'code': code
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    res = requests.post('https://kauth.kakao.com/oauth/token', data=data, headers=headers)
    token_json = res.json()
    print(token_json)
    access_token = token_json['access_token']

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    res = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
    profile_json = res.json()
    kakao_id = profile_json['id']
    user = User.objects.filter(email=kakao_id)
    print(user)
    if user.first() is not None:
        login(request, user.first(), backend='allauth.account.auth_backends.AuthenticationBackend')
    else:
        user = User()
        user.email = kakao_id
        user.username = profile_json['properties']['nickname']
        user.save()
        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

    return redirect('/board/list')
