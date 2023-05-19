from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from rest_framework import viewsets
from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)

class menuview(APIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data)    

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer 
    permission_classes = [permissions.IsAuthenticated]   
    
