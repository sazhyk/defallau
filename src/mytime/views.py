# -*- coding: utf-8 -*-
from django.shortcuts import render

from allauth.account.forms import LoginForm


def home(request):
    context = {
        'login_form': LoginForm
    }
    return render(request, 'home.html', context)
