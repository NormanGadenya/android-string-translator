# Generated by Django 4.1.1 on 2022-12-22 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0007_alter_filestatus_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
    ]