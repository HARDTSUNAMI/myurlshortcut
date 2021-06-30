from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES['default']: dj_database_url.config(default=os.getenv('DATABASE_URL'), conn_max_age=600)

django_heroku.settings(locals())
