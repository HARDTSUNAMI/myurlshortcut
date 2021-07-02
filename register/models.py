import random
import string
from typing import Any
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def link_generator(
    size: int = 12,
    chars: str = string.ascii_lowercase + string.digits + string.ascii_uppercase
) -> str:
    slug = ''.join(random.choice(chars) for _ in range(size))
    return slug


class LinkModel(models.Model):
    link = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    counter = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def get_absolute_url(self):
        return reverse('', kwargs={'link_slug': self.link})

    def __str__(self) -> str:
        return '{} {}'.format(self.slug, self.counter)

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.slug = link_generator()
        super(LinkModel, self).save(*args, **kwargs)
