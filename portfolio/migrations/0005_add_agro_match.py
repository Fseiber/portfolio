from django.db import migrations


def add_agro_match(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    database = schema_editor.connection.alias
    if not Project.objects.using(database).filter(slug="agro-match").exists():
        Project.objects.using(database).create(
            title="Agro Match",
            slug="agro-match",
            category="Hackathon · 1.er puesto",
            description=(
                "Proyecto desarrollado en equipo durante una hackathon, "
                "con el que obtuvimos el primer puesto. Explorá la demo para conocer la propuesta."
            ),
            url="https://agro-match-psi.vercel.app/",
            featured=True,
            order=0,
        )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0004_alter_project_description")]
    operations = [migrations.RunPython(add_agro_match, migrations.RunPython.noop)]
