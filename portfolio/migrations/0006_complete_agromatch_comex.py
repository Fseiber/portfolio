from django.db import migrations, models


def complete_agromatch(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Project.objects.using(schema_editor.connection.alias).filter(slug="agro-match").update(
        title="AgroMatch COMEX",
        category="NEA TECH 2026 · 1.er puesto AgriTech",
        description=(
            "Plataforma web para facilitar la comercialización y exportación de arroz del NEA, "
            "conectando molinos y proveedores con compradores nacionales e internacionales. "
            "Incluye matching comercial, marketplace, solicitudes, cotizaciones, cálculo de "
            "costos de exportación y seguimiento de operaciones. El equipo también desarrolló "
            "un prototipo experimental de contrato inteligente con Stellar y Soroban."
        ),
        contribution=(
            "Participé en la definición y evolución de la idea, el análisis del problema y "
            "las decisiones de producto. Trabajé en el diseño y las mejoras de la interfaz, "
            "las pruebas del sistema, la preparación de la presentación y el despliegue web "
            "mediante GitHub y Vercel. El equipo utilizó React, TypeScript y herramientas "
            "de desarrollo asistido por inteligencia artificial."
        ),
        tech_tags="React, TypeScript, Vercel, Stellar / Soroban (prototipo)",
        repo_url="https://github.com/Fseiber/AgroMatch",
        url="https://agro-match-psi.vercel.app/",
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0005_add_agro_match")]
    operations = [
        migrations.AddField(
            model_name="project",
            name="contribution",
            field=models.TextField(blank=True, verbose_name="Mi aporte"),
        ),
        migrations.RunPython(complete_agromatch, migrations.RunPython.noop),
    ]
