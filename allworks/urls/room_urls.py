from django.urls import path
from allworks.views.room_view import RoomListCreateView, RoomDetailView, RoomAvailabilityView

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='room_list'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('<int:pk>/availability/', RoomAvailabilityView.as_view(), name='room_availability'),
]
