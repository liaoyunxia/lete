# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.shortcuts import render

# Create your views here.
def share(request):
    title = '行程分享'
    return render(request, 'share.html', locals())


class JourneyView(generic.DetailView):
    '''
    行程首页
    '''
    template_name = 'index.html'

    def get_queryset(self):
        return None

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('/accounts/login/')
        template_name = self.template_name if self.template_name else '{}.html'.format(self.name)
        return render(request, template_name, locals())
