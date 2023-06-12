from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

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

    def retrieve(self, request, *args, **kwargs):
        room = Room.objects.filter(id=self.kwargs.get('pk')).first()
        if not room:
            return Response({'error': 'topilmadi'}, status=status.HTTP_404_NOT_FOUND)
