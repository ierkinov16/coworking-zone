from django.urls import path
from allworks.views.resident_view import ResidentDetailView, ResidentListCreateView

urlpatterns = [
    path('', ResidentListCreateView.as_view(), name='resident_list'),
    path('<int:pk>', ResidentDetailView.as_view(), name='resident_detail')
]
