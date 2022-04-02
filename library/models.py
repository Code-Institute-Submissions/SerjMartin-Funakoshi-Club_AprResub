from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=254)
    writer = models.CharField(max_length=254)
    description = models.TextField()
    link = models.CharField(max_length=254)

    def __str__(self):
        return self.name
