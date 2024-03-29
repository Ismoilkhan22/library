from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    isb = models.CharField(max_length=13)

    def __str__(self):
        return self.title
