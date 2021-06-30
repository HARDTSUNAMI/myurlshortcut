from .dev import *
import dj_database_url

DEBUG = False

DATABASES['default']: dj_database_url.config(default=os.getenv('DATABASE_URL'), conn_max_age=600)

django_heroku.settings(locals())

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    from .dev import *
except ImportError:
    pass
