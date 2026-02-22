from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudContactos', '0003_contactos_fijado_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='favorito',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='contactos/'),
        ),
    ]
