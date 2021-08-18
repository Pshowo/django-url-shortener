from django.db import models
from .utils import random_url_short

# Create your models here.
class Shortener(models.Model):
    time_added = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    url_long = models.URLField()
    url_short = models.CharField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return f"{self.url_short} - {self.url_long}"

    def save(self, *args, **kwargs):
        if not self.url_short:
            self.url_short = random_url_short(self)

        super().save(*args, **kwargs)