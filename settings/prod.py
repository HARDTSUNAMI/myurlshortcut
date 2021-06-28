from .base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://tophsgoaearpea:4edc29f30b0d92fd3cf9ae7ced2c97e396d4c1a1c6b70652616881259f745600@ec2-54-74'
                '-156 '
                '-137.eu-west-1.compute.amazonaws.com:5432/d7sjbu2ia00m8n',
        conn_max_age=600)}

django_heroku.settings(locals())
