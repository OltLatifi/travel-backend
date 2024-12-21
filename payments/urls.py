# urls.py
from django.urls import path
from .views import CreateFlightReservationView, CreatePaymentIntentView, GetBookingReservationsView, GetFlightReservationsView

urlpatterns = [
    path("create-payment-intent/", CreatePaymentIntentView.as_view(), name="create-payment-intent"),
    path("properties/", GetBookingReservationsView.as_view(), name="get-booking-reservations"),

    path("create-flight-reservation/", CreateFlightReservationView.as_view(), name="create-flight-reservation"),
    path("flights/", GetFlightReservationsView.as_view(), name="get-flight-reservations"),
]
