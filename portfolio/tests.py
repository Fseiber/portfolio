from django.test import TestCase
from django.urls import reverse

from .models import Project


class FeaturedProjectsTests(TestCase):
    def test_all_featured_projects_are_accessible(self):
        Project.objects.all().delete()
        for index in range(4):
            Project.objects.create(
                title=f"Proyecto {index}", featured=True, order=index,
            )
        response = self.client.get(reverse("portfolio:home"))
        for index in range(4):
            self.assertContains(response, f"Proyecto {index}")
