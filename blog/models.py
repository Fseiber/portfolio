import datetime

from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images/", blank=True)
    external_url = models.URLField("Enlace a publicación externa", blank=True, max_length=500)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.external_url or reverse("blog:post_detail", args=[self.pk])
