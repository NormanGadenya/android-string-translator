# Generated by Django 4.1.1 on 2022-12-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0006_remove_session_new_file_name_session_translatedtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestatus',
            name='status',
            field=models.FloatField(),
        ),
    ]
