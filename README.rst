=================
Django Hitcounter
=================

.. image:: https://badges.gitter.im/MrYodda/DirectlineDev.svg
    :target: https://gitter.im/MrYoda/DirectlineDev?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://badge.fury.io/gh/DirectlineDev%2Fdjango-hitcounter.svg
    :target: http://badge.fury.io/gh/DirectlineDev%2Fdjango-hitcounter

.. image:: https://travis-ci.org/DirectlineDev/django-hitcounter.svg?branch=master
    :target: https://travis-ci.org/DirectlineDev/django-hitcounter

.. image:: https://badge.fury.io/py/djangohitcounter.svg
    :target: http://badge.fury.io/py/djangohitcounter

.. image:: https://coveralls.io/repos/DirectlineDev/django-hitcounter/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/DirectlineDev/django-hitcounter?branch=master



About
-----

Pretty simple hit counter for Django ORM objects. It collects hits for any django model objects per date.

Requirements
------------

* Python 2 & 3
* Django 1.7+

Installation
------------

1. Install it using pip (coming soon):

.. code:: sh

 pip install djangohitcounter


or add ``django_hitcounter`` to your Python path

2. Add the ``django_hitcounter`` app to your ``INSTALLED_APPS``:

.. code:: python

  # settings.py
  INSTALLED_APPS = (
    ...,
    'django_hitcounter',
    ...
  )


Usage
-----

Usage is pretty simple too.

.. code:: python

  from django_hitcounter.models import Counter
  from datetime import datetime, timedelta


  obj = SomeModel.objects.get(pk=1)  # get some django object

  Counter.hit(obj)  # register hit
  Counter.hit(obj, amount=2)  # register 2 hits
  Counter.hit(obj, date=datetime.today().date() - timedelta(days=1))  # register hit on yesterday date

  Counter.objects.for_model(obj)  # get all counter records for our object
  Counter.objects.for_model(obj, total=True)  # get total hits count for object


License
-------

This software is distributed under the Apache License Version 2.0
