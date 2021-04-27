from django.contrib import admin
from .models import LinkModel


class UrlsAdmin(admin.ModelAdmin):  # type:ignore
    list_display = ('link', 'slug', 'counter', 'user', 'created_at')


admin.site.register(LinkModel)
