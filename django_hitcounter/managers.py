# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_text
from django.db.models import Sum


__all__ = ['CounterManager', ]


class CounterManager(models.Manager):

    def for_model(self, model, total=False):
        """
        QuerySet for all counter records for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_queryset().filter(content_type=ct)
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_text(model._get_pk_val()))
        if total:
            qs = qs.aggregate(Sum('hits'))['hits__sum']
        return qs
