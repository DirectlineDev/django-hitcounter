# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('object_pk', models.TextField(verbose_name='object ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='hits count')),
                ('content_type', models.ForeignKey(verbose_name='application', to='contenttypes.ContentType', related_name='content_type_set_for_counter')),
            ],
            options={
                'verbose_name': 'counter',
                'verbose_name_plural': 'counters',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='counter',
            unique_together=set([('content_type', 'object_pk', 'date')]),
        ),
    ]
