from settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shortcut',
        'USER': 'postgres',
        'PASSWORD': 'secretsecretpassword',
        'HOST': 'database',
        'PORT': '5432',
    }
}
