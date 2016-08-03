# -*- coding: utf-8 -*-
from django.shortcuts import render

from allauth.account.forms import LoginForm, SignupForm


def home(request):
    context = {
        'login_form': LoginForm
    }
    return render(request, 'home.html', context)


def register(request):
    context = {
        'signup_form': SignupForm
    }
    return render(request, 'register.html', context)
