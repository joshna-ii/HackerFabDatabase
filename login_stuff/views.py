from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.utils import timezone

from socialnetwork.forms import LoginForm, RegisterForm

from socialnetwork.MyMemoryList import MyMemoryList

ENTRY_LIST = MyMemoryList()

@login_required
def global_action(request):
    context = {}
    context['Name'] = f"{request.user.first_name} {request.user.last_name}"
    return render(request, 'global.html', context)

@login_required
def follower_action(request):
    context = {}
    context['Name'] = f"{request.user.first_name} {request.user.last_name}"
    return render(request, 'follower.html', context)

@login_required
def mypfp_action(request):
    context = {}
    context['Name'] = f"{request.user.first_name} {request.user.last_name}"
    return render(request, 'mypfp.html', context)

@login_required
def otherpfp_action(request):
    context = {}
    context['Name'] = f"{request.user.first_name} {request.user.last_name}"
    return render(request, 'otherpfp.html', context)

def login_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'login.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = LoginForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
   
    login(request, new_user)
    context['Name'] = f"{request.user.first_name} {request.user.last_name}"
    return render(request, 'global.html', context)


def logout_action(request):
    logout(request)
    return redirect(reverse('login'))


def register_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, 'register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegisterForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    context['Name'] = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}"
    login(request, new_user)
    return render(request, 'global.html', context)