from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from allworks.models.room import Room
from pagination import CustomPageNumberPagination
from allworks.serializer.room_serializer import RoomListSerializer, RoomDetailSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.order_by('-id')
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = ('id', 'name')
    search_fields = ('name',)
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RoomListSerializer
        else:
            return RoomDetailSerializer


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RoomListSerializer
        return RoomDetailSerializer
