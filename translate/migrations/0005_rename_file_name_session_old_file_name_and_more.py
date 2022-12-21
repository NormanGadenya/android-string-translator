# Generated by Django 4.1.1 on 2022-11-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0004_filestatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='file_name',
            new_name='old_file_name',
        ),
        migrations.AddField(
            model_name='session',
            name='new_file_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]