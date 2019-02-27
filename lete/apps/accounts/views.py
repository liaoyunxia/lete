# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.template.defaultfilters import lower
from django.contrib.auth.decorators import login_required


from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework_xml.parsers import XMLParser
# from rest_framework import generics


from django.shortcuts import render
import json

# Create your views here.

	# url(r'^login/$', views.login),
	# url(r'^logout/$', views.logout),
 #    url(r'^register/$', views.caculater),
 #    url(r'^update_password/$', views.update_password),


def login(request):
 	return render(request, 'login.html', locals())


def update_password(request):
 	return render(request, 'update_password.html', locals())


def logout(request):
 	auth.logout(request)
 	return HttpResponseRedirect('/')


def register(request):
 	return render(request, 'register.html', locals())


def login_action(request):
 	username = request.POST.get('username')
 	password = request.POST.get('password')
 	print('username=%s, password=%s'%(username, password))
 	user = auth.authenticate(username=username, password=password)
 	if user:
 		auth.login(request, user)
 		user.backend = 'django.contrib.auth.backends.ModelBackend'
 		print('1111111111')
 		return HttpResponseRedirect('/')
 	else:
 		print('2222222222')
 		return HttpResponse({'code': 10001, 'msg': 'not found user'}, content_type='application/json')

