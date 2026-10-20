from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "order")
    list_editable = ("featured", "order")
    list_filter = ("featured", "category")
    prepopulated_fields = {"slug": ("title",)}
