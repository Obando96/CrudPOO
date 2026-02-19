from django.db import migrations, models


def asignar_orden_fijados(apps, schema_editor):
    Contactos = apps.get_model('crudContactos', 'Contactos')
    orden = 1
    for contacto in Contactos.objects.filter(fijado=True).order_by('created', 'id'):
        if contacto.fijado_orden is None:
            contacto.fijado_orden = orden
            contacto.save(update_fields=['fijado_orden'])
            orden += 1


class Migration(migrations.Migration):

    dependencies = [
        ('crudContactos', '0002_contactos_fijado'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='fijado_orden',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.RunPython(asignar_orden_fijados, migrations.RunPython.noop),
    ]
