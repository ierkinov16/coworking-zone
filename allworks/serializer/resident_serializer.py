from rest_framework import serializers
from allworks.models import Resident


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ('name', 'email')
        read_only_fields = ('id',)


