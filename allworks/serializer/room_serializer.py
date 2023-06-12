from rest_framework import serializers
from allworks.models import Room


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'type', 'capacity')
        read_only_fields = ('id',)


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'type', 'capacity')
        read_only_fields = ('id',)
