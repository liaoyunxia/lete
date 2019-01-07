# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from common.models import UserModel, TimeModel, StateModel

ARTICLE_IMPORT_METHOD_CHOICES = ((0, ' 用户编辑'), (1, '爬虫获取'), (2, '用户复制'))


class Article(UserModel, TimeModel, StateModel):
    url = models.CharField(_('url'), max_length=100, blank=True)
    import_mothon = models.IntegerField(_('import_method'), choices=ARTICLE_IMPORT_METHOD_CHOICES, default=0)
    name = models.CharField(_('name'), max_length=50)
    key_word = models.CharField(_('key_word'), max_length=150, blank=True, default='')

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('article')