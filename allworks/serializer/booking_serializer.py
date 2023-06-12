from rest_framework import serializers
from allworks.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('room', 'resident')
