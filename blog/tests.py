from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogPagesTests(TestCase):
    def test_empty_list_uses_supported_reveal_class(self):
        Post.objects.all().delete()
        response = self.client.get(reverse("blog:posts"))
        self.assertContains(response, "Todavía no hay publicaciones.")
        self.assertContains(response, 'class="section shell reveal"')
        self.assertNotContains(response, "data-reveal")

    def test_post_is_listed_and_detail_uses_supported_reveal_class(self):
        post = Post.objects.create(title="Una experiencia", description="Lo que aprendí.")
        listing = self.client.get(reverse("blog:posts"))
        self.assertContains(listing, reverse("blog:post_detail", args=[post.pk]))
        detail = self.client.get(reverse("blog:post_detail", args=[post.pk]))
        self.assertContains(detail, post.title)
        self.assertContains(detail, post.description)
        self.assertContains(detail, 'class="article shell reveal"')
        self.assertNotContains(detail, "data-reveal")

    def test_external_publication_links_from_home_and_blog(self):
        post = Post.objects.create(
            title="Publicación externa", description="Una experiencia compartida.",
            external_url="https://www.linkedin.com/posts/example/",
        )
        for route in ("portfolio:home", "blog:posts"):
            response = self.client.get(reverse(route))
            self.assertContains(response, f'href="{post.external_url}"')
            self.assertContains(response, 'target="_blank" rel="noopener noreferrer"')
            self.assertNotContains(response, f'href="{reverse("blog:post_detail", args=[post.pk])}"')
