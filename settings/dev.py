from firstsite.settings.base import *
import dj_database_url

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
