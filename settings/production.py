from settings.base import *
import django_heroku
import dj_database_url


django_heroku.settings(locals())

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
