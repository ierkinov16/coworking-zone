from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from pagination import CustomPageNumberPagination
from allworks.serializer.booking_serializer import Booking, BookingSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.order_by('-id')
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = ('id', 'room')
    search_fields = ('room',)
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingSerializer
        else:
            return Booking


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingSerializer
        return Booking
