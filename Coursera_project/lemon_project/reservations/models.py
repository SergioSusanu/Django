from django.db import models

# Create your models here.
class Reservation(models.Model):
    date = models.DateField()
    guests = models.IntegerField()
    table = models.IntegerField()

    def __str__(self):
        return str(self.date) + "  " + str(self.guests)