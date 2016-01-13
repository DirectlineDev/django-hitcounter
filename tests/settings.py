SECRET_KEY = '_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django_hitcounter',
    'test_app',
)

ROOT_URLCONF = 'urls'

MIDDLEWARE_CLASSES = ()

