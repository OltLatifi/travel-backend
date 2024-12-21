from django.shortcuts import render
import stripe
from django.conf import settings

from flights.models import Flight
from notifications.models import Notification
from payments.models import BookingReservation, FlightReservation
from payments.serializers import BookingReservationSerializer, FlightReservationSerializer
from properties.models import Property

stripe.api_key = settings.STRIPE_SECRET_KEY

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreatePaymentIntentView(APIView):
    def post(self, request):
        try:
            property_id = request.data.get("property")
            nights = request.data.get("nights")
            customer_name = request.data.get("customer_name")
            payment_method_id = request.data.get("payment_method_id")

            property_obj = Property.objects.get(id=property_id)
            amount = int(property_obj.price_per_night * nights * 100)

            booking_reservation = BookingReservation.objects.create(
                property=property_obj,
                nights=nights,
                customer_name=customer_name,
                user=request.user,
                amount=amount,
            )
            
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                payment_method_types=["card"],
                payment_method=payment_method_id,
                confirm=True,
            )

            booking_reservation.completed = True
            booking_reservation.save()

            property_obj.available = False
            property_obj.save()

            Notification.objects.create(
                user=property_obj.host,
                content=f"{request.user.username} has booked your property \"{property_obj.name}\" for {nights} night(s).",
            )
            
            return Response({
                "client_secret": intent["client_secret"]
            })
        except stripe.error.StripeError as e:

            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CreateFlightReservationView(APIView):
    def post(self, request):
        try:
            flight_id = request.data.get("flight")
            seats = request.data.get("seats")
            customer_name = request.data.get("customer_name")
            payment_method_id = request.data.get("payment_method_id")

            flight = Flight.objects.get(id=flight_id)
            amount = int(flight.price_per_ticket * seats)

            flight_reservation = FlightReservation.objects.create(
                flight=flight,
                seats=seats,
                customer_name=customer_name,
                user=request.user,
                amount=amount,
            )
            
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                payment_method_types=["card"],
                payment_method=payment_method_id,
                confirm=True,
            )

            flight_reservation.completed = True
            flight_reservation.save()


            return Response({
                "client_secret": intent["client_secret"]
            })
        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetBookingReservationsView(APIView):
    def get(self, request):
        booking_reservations = BookingReservation.objects.filter(user=request.user).order_by("-created_at")
        serializer = BookingReservationSerializer(booking_reservations, many=True)
        return Response(serializer.data)

class GetFlightReservationsView(APIView):
    def get(self, request):
        flight_reservations = FlightReservation.objects.filter(user=request.user).order_by("-created_at")
        serializer = FlightReservationSerializer(flight_reservations, many=True)
        return Response(serializer.data)
