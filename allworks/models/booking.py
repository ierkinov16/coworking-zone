from django.db import models
from django.utils.translation import gettext_lazy as _


class Booking(models.Model):
    room = models.ForeignKey("allworks.Room", on_delete=models.CASCADE, related_name='bookings')
    resident = models.ForeignKey("allworks.Resident", on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField(_('Start Date', ))
    end_date = models.DateField(_('End Date', ))
    created = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.resident} - {self.room}'
