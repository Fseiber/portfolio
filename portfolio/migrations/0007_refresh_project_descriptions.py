from django.db import migrations


def refresh_projects(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    projects = Project.objects.using(schema_editor.connection.alias)
    projects.filter(slug="codix").update(
        title="Playcode",
        slug="playcode",
        category="Educación · Aplicación web",
        repo_url="https://github.com/mimbicaceres/playcode-app",
        description=(
            "Aplicación educativa para aprender conceptos de programación a través de "
            "la práctica. Reúne ejercicios interactivos, recorridos de aprendizaje "
            "adaptativos y gestión de usuarios en una misma experiencia."
        ),
        contribution=(
            "Trabajé en la lógica interactiva de los ejercicios y en el maquetado "
            "de los recorridos educativos."
        ),
    )
    projects.filter(slug="sistema-gestion-cursos").update(
        description=(
            "Aplicación web para centralizar la administración de alumnos, inscripciones "
            "y materiales de cursos. Desarrollada con Django, incorpora autenticación, "
            "permisos para administradores y estudiantes, y un panel para crear, "
            "consultar, editar y eliminar registros."
        ),
    )
    projects.filter(slug="el-universo-pos").update(
        description=(
            "Sistema de punto de venta para organizar las operaciones de un comercio. "
            "Integra un catálogo de productos, registro de ventas, control de stock "
            "y gestión de caja, con un historial de transacciones para consultar "
            "los movimientos del negocio."
        ),
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0006_complete_agromatch_comex")]
    operations = [migrations.RunPython(refresh_projects, migrations.RunPython.noop)]
