# Generated by Django 3.1.2 on 2020-12-19 00:23

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0011_auto_20201218_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='archivo',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage('C:\\Users\\trilo\\Django\\preguntas/static'), upload_to=''),
        ),
    ]
