from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=100000)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    complexity = models.CharField(max_length=50)
    deadline = models.DateTimeField()

