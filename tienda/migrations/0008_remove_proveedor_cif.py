# Generated by Django 4.0.6 on 2022-09-22 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_remove_proveedor_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='cif',
        ),
    ]