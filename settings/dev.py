from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shortcut',
        'USER': 'admin',
        'PASSWORD': 'secret',
        'HOST': 'database',
        'PORT': '5432',
    }
}
