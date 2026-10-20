import datetime

from django.db import migrations, models


def add_linkedin_post(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Post.objects.using(schema_editor.connection.alias).get_or_create(
        external_url=(
            "https://www.linkedin.com/posts/facundo-seiber_"
            "neatech2026-agrotech-desarrollodesoftware-ugcPost-7517758780000940032-tsoi/"
        ),
        defaults={
            "title": "AgroMatch COMEX: primer puesto en AgriTech en NEA TECH 2026",
            "description": (
                "Nuestra experiencia con AgroMatch COMEX, el proyecto con el que "
                "obtuvimos el primer puesto en la categoría AgriTech de NEA TECH 2026. "
                "Leé la publicación original en LinkedIn."
            ),
            "date": datetime.date(2026, 10, 20),
        },
    )


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial")]
    operations = [
        migrations.AddField(
            model_name="post", name="external_url",
            field=models.URLField(blank=True, max_length=500, verbose_name="Enlace a publicación externa"),
        ),
        migrations.AlterField(
            model_name="post", name="image",
            field=models.ImageField(blank=True, upload_to="blog/images/"),
        ),
        migrations.RunPython(add_linkedin_post, migrations.RunPython.noop),
    ]
