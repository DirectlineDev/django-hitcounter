# -*- coding: utf-8 -*-
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models, transaction
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from .managers import CounterManager


__all__ = ['Counter', ]


@python_2_unicode_compatible
class Counter(models.Model):
    """ Hits counter per date
    """
    # Content-object field
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for_%(class)s")
    object_pk = models.TextField(_('object ID'))
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    date = models.DateField(default=timezone.now, verbose_name=_('date'))
    hits = models.PositiveIntegerField(default=0, verbose_name=_('hits count'))

    # Manager
    objects = CounterManager()

    class Meta:
        verbose_name = _('counter')
        verbose_name_plural = _('counters')
        unique_together = (('content_type', 'object_pk', 'date'), )

    def __str__(self):
        return '{date}: {hits}'.format(
            date=self.date.strftime('%d-%m-%Y'),
            hits=self.hits
        )

    @classmethod
    def hit(cls, obj, amount=1, date=None):
        """ Increase hits counter for particular object on date (now() by default)
        :param obj: model object
        :param amount: increase amount (1 by default)
        :return: None
        """
        ct = ContentType.objects.get_for_model(obj)
        date = date or timezone.now()
        cls.objects.update_or_create(content_type=ct, object_pk=obj._get_pk_val(), date=date,
                                     defaults={'hits': F('hits')+amount})



