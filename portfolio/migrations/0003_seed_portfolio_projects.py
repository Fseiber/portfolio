from django.db import migrations


PROJECTS = [
    {
        "title": "Codix",
        "slug": "codix",
        "category": "Proyecto principal · Aplicación web",
        "description": (
            "Problema: herramienta dinámica para aprender conceptos de programación. "
            "Solución: módulos de ejercitación, flujos adaptativos y gestión de usuarios. "
            "Aporte: lógica interactiva del sistema y maquetado de flujos educativos."
        ),
        "tech_tags": "JavaScript, Node.js, Express, HTML/CSS, SQL",
        "order": 1,
    },
    {
        "title": "Sistema de Gestión de Cursos",
        "slug": "sistema-gestion-cursos",
        "category": "Académico · Full stack",
        "description": (
            "Problema: administrar alumnos, inscripciones y materiales. Solución: app monolítica "
            "en Django con panel de administración, autenticación y permisos por roles. "
            "Funcionalidades: CRUD completo, roles admin/estudiante y consultas SQL optimizadas."
        ),
        "tech_tags": "Python, Django, HTML/CSS, MySQL/SQLite",
        "order": 2,
    },
    {
        "title": "El Universo POS",
        "slug": "el-universo-pos",
        "category": "Desarrollo comercial · Gestión",
        "description": (
            "Problema: control de inventario, facturación rápida y ventas en comercio físico. "
            "Solución: software con reglas de negocio reales para stock y caja. "
            "Funcionalidades: registro de ventas, catálogo de productos e historial de transacciones."
        ),
        "tech_tags": "",
        "order": 3,
    },
]


def seed_projects(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    if Project.objects.exists():
        return
    for project in PROJECTS:
        Project.objects.create(featured=True, **project)


def remove_seeded_projects(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    Project.objects.filter(slug__in=[project["slug"] for project in PROJECTS]).delete()


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0002_alter_project_options_project_category_and_more")]
    operations = [migrations.RunPython(seed_projects, remove_seeded_projects)]
