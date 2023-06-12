from django.db import models


class Booking(models.Model):
    room = models.ForeignKey("allworks.Room", on_delete=models.CASCADE, related_name='bookings')
    resident = models.ForeignKey("allworks.Resident", on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.resident} - {self.room}'
