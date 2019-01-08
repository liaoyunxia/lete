"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from os.path import join, exists
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'', include('{}.apps.home.urls'.format(settings.PROJECT_NAME))),
    url(r'^api/v1/', include('{}.apps.api.urls'.format(settings.PROJECT_NAME), namespace='v1')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

apps_dir = join(settings.PROJECT_PATH, 'apps')
for dirname in next(os.walk(apps_dir))[1]:
    if dirname not in ['__pycache__', 'api', 'home'] and exists(join(apps_dir, '{}/urls.py'.format(dirname))):
        urlpatterns += [url(r'^{}/'.format(dirname), include('{}.apps.{}.urls'.format(settings.PROJECT_NAME, dirname)))]
