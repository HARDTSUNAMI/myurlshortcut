from settings.base import *
import django_heroku
import dj_database_url


django_heroku.settings(locals())

DEBUG = True

DATABASES['default'] = dj_database_url.config()
