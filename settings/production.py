from firstsite.settings.dev import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {'default': dj_database_url.config()
             }
