from django.urls import path
from .views import (
    VehicleListCreateView, VehicleDetailView,
    VehicleBookingListCreateView, VehicleBookingDetailView
)

urlpatterns = [
    path('', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),

    path('bookings/', VehicleBookingListCreateView.as_view(), name='vehicle-booking-list-create'),
    path('bookings/<int:pk>/', VehicleBookingDetailView.as_view(), name='vehicle-booking-detail'),
]
