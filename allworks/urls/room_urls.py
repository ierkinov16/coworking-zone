from django.urls import path
from allworks.views.room_view import RoomListCreateView, RoomDetailView

urlpatterns = [
    path('', RoomListCreateView.as_view(), name='room_list'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
]
