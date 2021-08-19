from django.db import models

# Create your models here.
class Shortener(models.Model):
    time_added = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    url_long = models.URLField()
    url_short = models.CharField(max_length=150, blank=True, unique=True)
    user_ip = models.CharField(max_length=12, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.url_short} - {self.url_long}"
