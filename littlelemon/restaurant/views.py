from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateView, RetrieveUpdateDestroyAPIView
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

class MenuItemView(generics.ListCreateView):
    pass

class SinlgeItemView(generics.RetrieveUpdateDestroyAPIView):
    pass
