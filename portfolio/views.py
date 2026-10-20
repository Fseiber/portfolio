from django.shortcuts import render

from blog.models import Post

from .models import Project


def home(request):
    projects = Project.objects.filter(featured=True)
    if not projects:
        projects = Project.objects.all()[:3]
    posts = Post.objects.all()[:3]
    return render(request, "portfolio/home.html", {"projects": projects, "posts": posts})
