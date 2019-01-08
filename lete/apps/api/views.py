# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from django.shortcuts import render

# Create your views here.
def caculater(request):
    title = '计算器'
    return render(request, 'caculater.html', locals())

