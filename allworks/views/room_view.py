from datetime import timezone

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from allworks.models import Booking
from allworks.models.room import Room
from allworks.serializer.room_serializer import RoomListSerializer, RoomDetailSerializer
from pagination import CustomPageNumberPagination


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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RoomListSerializer
        return RoomDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        room = Room.objects.filter(id=self.kwargs.get('pk')).first()
        if not room:
            return Response({'error': 'topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        return super().retrieve(request, *args, **kwargs)


class RoomAvailabilityView(ListAPIView):
    def list(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')
        today = timezone.now()
        data = []
        bookings = (
            Booking.objects.filter(room_id=room_id, start_date=today.date(), end_date=today.date())
            .order_by('start').values("resident_name", "start_hour", "end_hour")
        )
        if bookings:
            first_booking_start_hour = bookings[0].get("start_hour") if bookings else 23

        if 9 <= first_booking_start_hour:
            data.append({
                "resident": bookings[0].get("resident__name"),
                "start": "9:00",
                "end": f"{first_booking_start_hour}:00"
            })

        for i in range(len(bookings) - 1):
            start_hour = bookings[i].get("end__hour")
            end_hour = bookings[i + 1].get("start__hour")
            if start_hour != end_hour:
                data.append({
                    "start": bookings[i].get("resident_name"),
                    "start": f"{start_hour}:00",
                    "end": f"{end_hour}:00"
                })

        last_booking_end_hour = bookings.last().get("end__hour") if bookings else 9
        if last_booking_end_hour <= 23:
            data.append({
                "resident": bookings.last().get("resident__name"),
                "start": f"{last_booking_end_hour}:00",
                "end": "23:00"
            })

        return Response(data)
