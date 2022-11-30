from django.utils import timezone

from django.db import models


# Create your models here.


class Language(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Session(models.Model):
    source = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    date_initiated = models.DateTimeField(default=timezone.now)
    old_file_name = models.CharField(max_length=100, default='')
    new_file_name = models.CharField(max_length=100, default='')


class FileStatus(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.IntegerField()

