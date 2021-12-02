from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.name} your place successful booked"
