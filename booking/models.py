from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Booked"))


class Booking(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.name} your place successful booked"
