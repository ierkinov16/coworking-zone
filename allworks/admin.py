from django.contrib import admin

from allworks.models.booking import Booking
from allworks.models.resident import Resident
from allworks.models.room import Room

# Register your models here.
admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(Booking)
