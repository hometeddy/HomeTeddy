__author__ = 'Zhang_Rui'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from .forms import RegistrationForm, loginForm, EditProfileForm
from django.core.checks import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # create form object
        if form.is_valid():
            form.save()
            # messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/dashboard/')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()

    return render(request, 'account/register.html', args)


def login_view(request):
    if request.method == 'POST':
        form = loginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,
                                password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return HttpResponseRedirect('/search/')

            else:
                return HttpResponseRedirect('/search/')

    args = {}
    args.update(csrf(request))
    args['form'] = loginForm()

    return render(request, 'account/login.html', args)


@login_required()
def edit_user_profile(request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance= request.user.profile)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/account/EditProfile/')
        else:
            user = request.user
            profile = user.profile
            form = EditProfileForm(instance = profile)

        args = {}
        args.update(csrf(request))
        args['form'] = form

        return render(request, 'account/EditProfile.html', args)