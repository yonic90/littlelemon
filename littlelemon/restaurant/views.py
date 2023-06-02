from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets, views
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from .permissions import IsAdmin, IsManager, IsCustomer, ReadOnly

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin, IsManager]
        return [permission() for permission in permission_classes]  

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        if self.request.method in ["GET", "POST"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin, IsManager]
        return [permission() in permission in permission_classes]  
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer                    

