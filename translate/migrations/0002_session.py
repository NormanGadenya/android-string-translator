# Generated by Django 4.1.1 on 2022-11-28 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=10)),
                ('date_initiated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
