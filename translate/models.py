from django.utils import timezone

from django.db import models


# Create your models here.

class Session(models.Model):
    source = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    date_initiated = models.DateTimeField(default=timezone.now)
    old_file_name = models.CharField(max_length=100, default='')
    translatedText = models.TextField()


class FileStatus(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.FloatField()

