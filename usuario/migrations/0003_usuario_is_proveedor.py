# Generated by Django 4.0.6 on 2022-09-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_rename_usuario_activo_usuario_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_proveedor',
            field=models.BooleanField(default=False),
        ),
    ]
