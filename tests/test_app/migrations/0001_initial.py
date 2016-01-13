# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dummy_field', models.IntegerField(verbose_name='dummy field')),
            ],
            options={
                'verbose_name_plural': 'dummy model',
                'verbose_name': 'dummy model',
            },
        ),
    ]
