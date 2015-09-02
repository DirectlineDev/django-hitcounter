=================
Django Hitcounter
=================

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


  obj = SomeModel.objects.get(pk=1)  # get some django object

  Counter.hit(obj)  # register one hit
  Counter.hit(obj, amount=2)  # register 2 hits

  Counter.objects.for_model(obj)  # get all counter records for our object
  Counter.objects.for_model(obj, total=True)  # get total hits count for object


License
-------

This software is distributed under the Apache License Version 2.0
