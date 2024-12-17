# urls.py
from django.urls import path
from .views import CreatePaymentIntentView, GetBookingReservationsView

urlpatterns = [
    path("create-payment-intent/", CreatePaymentIntentView.as_view(), name="create-payment-intent"),
    path("properties/", GetBookingReservationsView.as_view(), name="get-booking-reservations"),
]
