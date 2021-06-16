from django.contrib import admin
from .models import LinkModel


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('link', 'slug', 'counter', 'user', 'created_at')


admin.site.register(LinkModel)
