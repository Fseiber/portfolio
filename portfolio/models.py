from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    contribution = models.TextField("Mi aporte", blank=True)
    image = models.ImageField(upload_to="portfolio/images/", blank=True)
    url = models.URLField(blank=True)
    slug = models.SlugField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    tech_tags = models.CharField(max_length=250, blank=True)
    repo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    @property
    def tech_tag_list(self):
        return [tag.strip() for tag in self.tech_tags.split(",") if tag.strip()]

    def __str__(self):
        return self.title
