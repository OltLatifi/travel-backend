from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Property, Booking, Image, Review
from .serializers import PropertySerializer, BookingSerializer, ImageSerializer, ReviewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ViewSet


class PropertyView(ViewSet):
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Property.objects.filter(host=request.user).prefetch_related('images')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            property = serializer.save()

            images = request.FILES.getlist('images')
            if images:
                for image in images:
                    Image.objects.create(property=property, image=image)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Property.objects.filter(id=pk).prefetch_related('images').first()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        property = Property.objects.get(id=pk)
        if not request.user == property.host:
            return Response({"message": "You are not authorized to update this property"}, status=403)
        
        serializer = self.serializer_class(property, data=request.data, partial=True)
        if serializer.is_valid():
            property = serializer.save()

            images = request.FILES.getlist('images')
            if images:
                for image in images:
                    Image.objects.create(property=property, image=image)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        property = Property.objects.get(id=pk)
        if not request.user == property.host:
            return Response({"message": "You are not authorized to delete this property"}, status=403)
        
        property.delete()
        return Response({"message": "Property deleted successfully"}, status=204)


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_properties(request):
    queryset = Property.objects.filter(available=True).prefetch_related('images')
    paginator = PageNumberPagination()
    paginator.page_size = 10

    result_page = paginator.paginate_queryset(queryset, request)

    serializer = PropertySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_property_availability(request, property_id):
    property_obj = Property.objects.get(id=property_id)
    if not request.user == property_obj.host:
        return Response({"message": "You are not authorized to update this property"}, status=403)
    
    property_obj.available = True
    property_obj.save()
    return Response({"message": "Property availability updated successfully"})
