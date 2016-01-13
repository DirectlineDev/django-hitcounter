# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class DummyModel(models.Model):
    """ Dummy model for tests
    """
    dummy_field = models.IntegerField(verbose_name='dummy field')

    class Meta:
        verbose_name = _('dummy model')
        verbose_name_plural = _('dummy model')
