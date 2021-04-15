import random
import string
from django.contrib.auth.models import User
from django.db import models


def link_generator(size=12, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
    slug = ''.join(random.choice(chars) for _ in range(size))
    return slug


class LinkModel(models.Model):
    link = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    counter = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return '{} {}'.format(self.slug, self.counter)

    def save(self, *args, **kwargs):
        self.slug = link_generator()
        super(LinkModel, self).save(*args, **kwargs)
